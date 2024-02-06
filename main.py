import psycopg2
from psycopg2 import Error
from fastapi import FastAPI

app = FastAPI()

#Creating connection to the database
try:
    connection = psycopg2.connect(user="postgres",
                              password="admin",
                              host="127.0.0.1",
                              port="5432",
                              database="userauthen")

    cursor = connection.cursor()
    create_table_query = """CREATE TABLE IF NOT EXISTS users 
    (
    id INT PRIMARY KEY ,
    lastname  varchar(255) NOT NULL,
    firstname varchar(255) NOT NULL,
    user_name varchar(255) NOT NULL,
    email varchar(50) NOT NULL,
    password varchar(50) NOT NULL);"""

    cursor.execute(create_table_query)
    connection.commit()
    print("table successfully created")
    

except(Exception, Error) as Error:
    print("Error while connecting to database", Error)


@app.get("/")
def read_root():
    return{"message:" "Welcome to register API"}


@app.get("/all_users/")
def read_users():
    cursor.execute("SELECT * from users")
    record = cursor.fetchall()
    return{"Result ": record}



#Register user    
@app.post("/register/")
async def register_user(id: int, lastname: str, firstname: str, user_name: str, email: str, password:str):
    insert_query = """INSERT INTO users(id, lastname, firstname, user_name,email, password) VALUES (%s, %s,%s, %s, %s,%s)"""
    values = (id, lastname,firstname, user_name, email, password)
    connection = psycopg2.connect(database="userauthen", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cursor = connection.cursor()
    
    try:
        cursor.execute(insert_query, values)
        connection.commit()
        return {"message": "Registration successful"}

            
    except psycopg2.Error as e:
        return{"Error:", e}

    finally:
        cursor.close()
        connection.close()



#login Section
@app.post("/login/")
async def log_in(user_name: str, password:str):
    log_in ="""SELECT user_name, password FROM users WHERE user_name = %s AND password = %s"""
    values = (user_name, password)

    connection = psycopg2.connect(database="userauthen", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cursor = connection.cursor()

    try:
        cursor.execute(log_in, values)
        record = cursor.fetchall()
        print("Result:", record)

        if record:
            return {"message": "Login successful"}
        else:
            return{"message": "Login not successful"}
        
    except psycopg2.Error as e:
        return{"Error:", e}
    


#change password
@app.put("/change_password")
async def change_password(user_name: str, password: str, new_password: str):
    check_old_password = """SELECT password FROM users WHERE user_name = %s"""
    change_password = """UPDATE users SET password = %s WHERE user_name = %s""" 
    values = (user_name, password)
    
    connection = psycopg2.connect(database="userauthen", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cursor = connection.cursor()

    try:
        cursor.execute(check_old_password, (user_name,))
        stored_password = cursor.fetchone()

        if stored_password and stored_password[0] == password:
                cursor.execute(change_password,(new_password, user_name))
                connection.commit()
                return {"message": "Password change successful"}
        else:
            return{"message": "Password change not successful"}
        
    except psycopg2.Error as e:
        return{"Error:", e}



@app.delete("/delete_user")
async def delete_user(id: int):
    delete_user = """DROP USER [IF EXISTS] id"""
    values = (id)

    connection = psycopg2.connect(database= "userauthen", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cursor = connection.cursor()

    try:
        cursor.execute(delete_user, values)
        connection.commit()
        return{"message": "User has been deleted"}
    except psycopg2.Error as e:
        return{"Error": e}




