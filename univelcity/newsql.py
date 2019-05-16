import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# name = "kayode"
# age = 32
# gender = "male"
# for i in range(50):
#     with connection.cursor() as cursor:
#         # print(row)
#         sql = """insert into students ( name, age, gender) 
#             values ("{}", "{}","{}")""".format(name, age, gender)
#         cursor.execute(sql)

#         connection.commit()


# with connection.cursor() as cursor:
#     # print(row)
#     sql = "CREATE TABLE TEST_TABLE (id int NOT NULL PRIMARY KEY AUTO_INCREMENT)"
#     cursor.execute(sql)

#     connection.commit()



with connection.cursor() as cursor:
    # print(row)
    sql = "SELECT * FROM STUDENTS"
    
    cursor.execute(sql)

    print(cursor.fetchall())