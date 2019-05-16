import pymysql.cursors

#
# connect to database
connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '$omerta2019',
                             db = 'db',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor

)

with connection.cursor() as cursor:
    #Create a new record
    # sql = """CREATE TABLE TEST(id int(3) primary key unique auto_increment, type VARCHAR(20)) """

    sql = """INSERT INTO TEST (type) VALUES ('PHYSICS') """

    cursor.execute(sql)
    connection.commit()