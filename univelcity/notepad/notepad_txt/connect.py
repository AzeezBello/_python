


# import pymysql.cursors


# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# def create_table():
#     #CREATE DATABASE
#     try:
#         with connection.cursor() as cursor:
#             # Create a new record

#             sql = """CREATE TABLE notes 
#                     (id int NOT NULL KEY AUTO_INCREMENT,
#                     username VARCHAR(100), 
#                     body VARCHAR(400), 
#                     title VARCHAR(100)
#                     )"""

#             cursor.execute(sql)
#             connection.commit()
#     except:
#         # connection is not autocommit by default. So you must commit to save
#         # your changes.

#         print('Table Exists')




# def add(row):
#     with connection.cursor() as cursor:
#         # print(row)
#         sql = """insert into notes 
#             (username,  title, body) 
#             values ("{}", "{}","{}")
#             """.format(row[0],row[1],row[2])

#         cursor.execute(sql)

#         connection.commit()

# def select(user):
#     with connection.cursor() as cursor:
#         # print(row)
#         sql = '''SELECT  title, body 
#                  FROM  notes WHERE 
#                 username = "{}"'''.format(user.username)

#         cursor.execute(sql)
#         return (cursor.fetchall())
#         # connection.commit()
