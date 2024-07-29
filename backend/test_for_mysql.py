from  flask import Flask
from connect_to_mysql import db,MyDatabase
app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
with app.app_context():#with app.app_context(): 语句用于在 Flask 应用中创建一个应用上下文，并在其中执行一系列操作，以确保这些操作能够在正确的环境中执行。
    db.create_all()
    data = {
    "title": "Test Title",
    "task": "summary",
    "content": "Test Content",
    "result": "Test Result"
    }
with app.app_context():
    mydatabase = MyDatabase(**data)
    db.session.add(mydatabase)
    db.session.commit()
    # 查询并打印所有数据
    mydata=db.session.query(MyDatabase).all()
    for data in mydata:
        print(data.to_dict())  # 使用 app.logger.info() 打印信息到后端日志