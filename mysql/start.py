import pymysql


# 打开数据库连接
db = pymysql.connect(host="139.196.10.197", port=3306, user="root", password="641541452",
                     database="learn", charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)
# SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % 'M'
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % 1000
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        firstName = row[0]
        lastName = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print(firstName, lastName, age, sex, income)
except:
    print(111)
# 关闭数据库连接
db.close()
