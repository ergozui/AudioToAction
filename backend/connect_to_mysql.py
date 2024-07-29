from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import bcrypt
db = SQLAlchemy()

class MyDatabase(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #主码自增
    save_time = db.Column(db.TIMESTAMP, default=db.func.current_timestamp()) #时间戳
    title = db.Column(db.Text, nullable=False) #主题
    task = db.Column(db.Enum('Key points identification','Action item extraction','summary', 'sentiment'), nullable=False) #选项
    content = db.Column(db.Text,nullable=False) #内容
    result=db.Column(db.Text) #结果
    u_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    other_table = db.relationship('MyUser')  # 关联到其他表

#声明子类属性
    # def __init__(self,title,task,content,result):
    #     self.title= title
    #     self.task = task
    #     self.content=content
    #     self.result=result
#类方法唯一实例化类
    def to_dict(self):
        return {
            "id": self.id,
            "save_time":self.save_time.strftime("%Y-%m-%d %H:%M:%S"),  # 将 datetime 对象转换为格式的字符串
            "title": self.title,
            "task": self.task,
            # "created_on": self.created_on.strftime("%Y-%m-%d %H:%M:%S"),
            "content": self.content,
            "result": self.result
        }
# #实例方法用于导出json
class MyUser(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #主码自增
    username=db.Column(db.Text, nullable=False)
    password_hash=db.Column(db.Text, nullable=False)
    register_time = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())  # 时间戳

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    def to_dict(self):
        return {
            "id": self.id,
            "username":self.username,
            "password": self.password_hash,
            "register_time": self.register_time.strftime("%Y-%m-%d %H:%M:%S"),
        }