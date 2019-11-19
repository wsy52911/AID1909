"""
使用数据库完成登录注册功能，数据表自己拟定

*注册方法：收集用户信息，将用户信息存储到数据库，用户名不能重复
*登录方法：获取用户名密码，与数据库信息比对，判定是否允许登录
"""
import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        # 判断该用户名是否存在
        sql = "select name from user where name='%s';"%name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False
        # 插入用户
        try:
            sql="insert into user (name,passwd) values (%s,%s)"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        sql = "select name,passwd from user \
        where name=%s and passwd=%s"
        self.cur.execute(sql,[name,passwd])
        result = self.cur.fetchone()
        if result:
            return True

if __name__ == '__main__':
    db = Database()
    # print(db.register('Lily','123'))
    print(db.login('Lily','1234'))










