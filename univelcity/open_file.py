# file = open("death_causes.csv", "r")

# index = 0
# for line in file:
#     index += 1
#     print(line.split(","))
    
#     if index == 3:
#         break
        

# # Year,Cause Name,Cause Name,State,Deaths,Age-adjusted Death Rate

# file = open("death_causes.csv", "r")
# deaths = 0
# count = 0
# for line in file:
#     if count == 0:
#         pass
#     else:
#         raw = line.split(",")
#         print(raw)
#         if raw[0] == "2014":
#             deaths += int(raw[4])
#     count += 1

 
# print(deaths/365)

# Year,Cause Name,Cause Name,State,Deaths,Age-adjusted Death Rate


# with open("twist.txt", "r") as file:
#     for line in file:
#         print(line)
# file.close()

import pymysql.cursors

class Mortality:
    
    def __init__(self, year,  cause_name_full, cause_name, state, deaths, age_adjusted_death_rate):
        self.year = (year)
        self.cause_name_full = cause_name_full
        self.cause_name = cause_name
        self.state = state
        self.deaths = (deaths)
        self.age_adjusted_death_rate = age_adjusted_death_rate[:-1]

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

def create_table(name):
    
    with connection.cursor() as cursor:
        # Create a new record
        try:
            sql = f"""CREATE TABLE {name} 
                    (id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    year INT(4), 
                    cause_name_full TEXT, 
                    cause_name TEXT, 
                    state VARCHAR(50), 
                    deaths VARCHAR(50), 
                    age_adjusted_death_rate VARCHAR(50))"""

            cursor.execute(sql)
            connection.commit()
        except:
            # connection is not autocommit by default. So you must commit to save
            # your changes.

            print('Table Exists')


def open_file():

    file = open("death_causes.csv", "r")

    count = 0

    for line in file:
        if count == 0:
            pass
        else:
            raw = line.split(",")
            # print(raw)
            new_mortality_object = Mortality( year = raw[0],  cause_name_full = raw[1], cause_name= raw[2], state = raw[3], deaths = raw[4], age_adjusted_death_rate = raw[5])

            post_to_db(new_mortality_object)
        count += 1
 
def post_to_db(mortality_object):

    with connection.cursor() as cursor:
        # Create a new record
       
        sql = f"""insert into mortality_rate (year,  cause_name_full, cause_name, state, deaths, age_adjusted_death_rate) 
            values ("{mortality_object.year}",  "{mortality_object.cause_name_full}", "{mortality_object.cause_name}", "{mortality_object.state}", "{mortality_object.deaths}", "{mortality_object.age_adjusted_death_rate}")"""
        # print(sql)

        cursor.execute(sql)
        connection.commit()

#CREATE TABLE IN DATABASE
create_table("mortality_rate")

#THEN PUSH FILES INTO TABLE
open_file()