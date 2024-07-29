#app.py
# -*- coding: utf-8 -*-
from flask import Flask,request, redirect, session,jsonify,make_response,send_file
import connect_to_openai as cto
from connect_to_mysql import db,MyDatabase,MyUser
import json
import flask_cors
from flask_cors import CORS,cross_origin
import os
import textract

from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=f"mysql+pymysql://root:1234@127.0.0.1/ai_log"
app.config['SECRET_KEY'] = 'abc'
db.init_app(app)
CORS(app,supports_credentials=True)
with app.app_context():#with app.app_context(): 语句用于在 Flask 应用中创建一个应用上下文，并在其中执行一系列操作，以确保这些操作能够在正确的环境中执行。
    db.create_all()

@app.route('/openai',methods=['post','get'])
@cross_origin()
def index():
    user_id=session.get('userid')
    if user_id:
        data=request.form
        title = data['title']
        task = data['type']
        content = data['content']
        print(title)
        print(task)
        print(content)
        if title == '' or task == '':
            return{'message': "没有上传值"}
        else:
        # 检查文件字段是否在请求中
            if content=='':
                file = request.files.get("file")
                if file is None:  # 表示没有发送文件
                    message = {'state': 'error'}
                    response = make_response(jsonify(message))
                    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
                    response.headers['Access-Control-Allow-Credentials'] = 'true'
                    return response
                else:
                    # 检查文件是否有文件名
                    if file.filename != '':
                        # 将文件名安全地保存到本地文件系统
                        filename = file.filename
                        file.save('uploads'+'/'+filename)
                        tyue_filename, ext = os.path.splitext(file.filename)
                        print(ext)
                        if(ext=='.mp3' or ext=='.mp4'):
                            print(tyue_filename)
                            content=cto.extract_audio(filename)
                            # result=cto.extract_audio2(file)
                            # 在这里可以将文件的其他信息保存到数据库中
                            result = cto.function_map[task](content)
                        else:
                            file_path=os.path.join('uploads/',filename)
                            content = textract.process(file_path).decode('utf-8')
                            result = cto.function_map[task](content)
            else:
                result=cto.function_map[task](content)
            print(result)
            data = {
                "title": title,
                "task": task,
                "content": content,
                "result": result,
                "u_id":user_id
            }
            with app.app_context():
                db.create_all()
                mydatabase = MyDatabase(**data)
                db.session.add(mydatabase)
                db.session.commit()
            message={'state':'success'}
            response = make_response(jsonify(message))
            # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            return response
    else:
        message = {'state': 'logerror'}
        response = make_response(jsonify(message))
        # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

@app.route('/history',methods=['post'])
def search():
    user_id = session.get('userid')
    if user_id:
        with app.app_context():
            db.create_all()
            mydata= MyDatabase.query.filter_by(u_id=user_id).all()
            data_list=[]
            for data in mydata:
                data_list.append(data.to_dict())
            json_data = json.dumps(data_list)
            print(json_data)
            return json_data
    else:
        message = {'state': 'error'}
        response = make_response(jsonify(message))
        # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        # response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
@app.route('/login',methods=['post'])
def find():
    data = request.form
    username = data['username']
    password = data['password']
    if username != '' and password != '':
        with app.app_context():
            db.create_all()
            user = MyUser.query.filter_by(username=username).first()
            if user:
                valid=user.check_password(password)
                if(valid):
                    session['userid']=user.id
                    session['username']=user.username
                    return jsonify({'state': "success"})
                else:
                    return jsonify({'state': "password error"})
            else:
                return jsonify({'state':'unexist user'})

    else:
        return jsonify({'state': 'please input'})
@app.route('/register',methods=['post'])
def insert():
    data = request.form
    username = data['username']
    password = data['password']
    if username!='' and password!='':
        with app.app_context():
            db.create_all()
            user_exists = MyUser.query.filter_by(username=username).first() is not None
            if user_exists:
                # 如果用户已经存在，直接返回错误信息
                return jsonify({'state': 'Username already registered'})
            else:
                myuser=MyUser(username=username)
                myuser.set_password(password)
                db.session.add(myuser)
                db.session.commit()
                mydata = db.session.query(MyUser).all()
                for data in mydata:
                    print(data.to_dict())  # 使用 app.logger.info() 打印信息到后端日志
                    return jsonify({'state':'success'})
    else:
        return jsonify({'state':'error'})
@app.route('/userinfo',methods=['post'])
def users():
    user_id = session.get('userid')
    if user_id:
        with app.app_context():
            db.create_all()
            myuser = MyUser.query.filter_by(id=user_id).first()
            mydata = MyDatabase.query.filter_by(u_id=user_id).all()
            length=len(mydata)
            data=myuser.to_dict()
            data['usetimes']=length
            data['state']='success'
            response = make_response(jsonify(data))
            return response
    else:
        message = {'state': 'error'}
        response = make_response(jsonify(message))
        return response
@app.route('/logout',methods=['post'])
def logout():
    session.clear()
    return jsonify({'state':'success'})
@app.route('/delete',methods=['post'])
def delete():
    user_id = session.get('userid')
    if user_id:
        data = request.form
        id = data['id']
        id=int(id)-1
        with app.app_context():
            mydata = MyDatabase.query.filter_by(u_id=user_id).all()
            data_to_delete=mydata[id]
            db.session.delete(data_to_delete)
            db.session.commit()
        return jsonify({'state': 'success'})
    else:
        message = {'state': 'error'}
        response = make_response(jsonify(message))
        return response
@app.route('/getaudio',methods=['post','get'])
def getaudio():
    user_id = session.get('userid')
    if user_id:
        file_path='uploads/speech.mp3'
        data = request.form
        analysis= data['analysis']
        cto.get_audio(analysis)
        response = make_response()
        # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return send_file(file_path)
    else:
        message = {'state': 'error'}
        response = make_response(jsonify(message))
        return response
if __name__ == '__main__':
    app.run('localhost', 5000,debug=True)
