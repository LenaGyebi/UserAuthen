import psycopg2
from psycopg2 import Error
from fastapi import FastAPI
import database
import getpass

#Creating connection to the database
try:
    connection = psycopg2.connect(user="postgres",
                              password="admin",
                              host="127.0.0.1",
                              port="5432",
                              database="userauthen")

    cursor=connection.cursor()
    print("PostgresSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version()")
    record = cursor.fetchone()
    print("You are connected to -", record, "\n")


    app = FastAPI()


    user_name = input("Please enter your username: ")
    email = input("enter your email: ")
    password = getpass.getpass("Enter your password: ")

except(Exception, Error) as Error:
    print("Eroor while connecting to database", Error)




#inserting the values into the database
    cursor = connection.cursor()
    insert_query = """INSERT INTO userauthen (id, user_name,email, password) VALUES (%s, %s, %s,%s)""", 
    (id, user_name, email, getpass)
    cursor.execute(insert_query)
    connection.commit()
    print("Values have been added to the table successfully")

    cursor.execute("SELECT * from userauthen")
    record = cursor.fetchall()
    print("Result: ", record)



finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Database has been closed")
                                                                                              
# for i in database():
#         if username == i:
#             if password != database.get(i):
#                 password = getpass.getpass("Please enter the password again: ")
#                 break 
#             print("Varified! Access granted")
#             while password != database.get(i):
#                 password = getpass.getpass("Please re-enter password: ")
#                 break
#             print("Verified! Access Granted!")
#             if password == j:
#                 print("Verified! Access granted")
#             else:
#                 print("Access Denied")


# @app.get("/root")
# async def root():
#     return("this is first data")