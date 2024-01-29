from fastapi import FastAPI

import getpass


app = FastAPI()



database = {'abena': '2345', 'Lena':'iwantto', 'Adlai':'ishetheone'}

# username = input("Please enter your username: ")
# password = getpass.getpass("Enter your password: ")

# for i in database.keys():
#         if username == i:
#             if password != database.get(i):
#                 password = getpass.getpass("Please enter the password again: ")
#                 break 
#             print("Varified! Access granted")
            # while password != database.get(i):
            #     password = getpass.getpass("Please re-enter password: ")
            #     break
            # print("Verified! Access Granted!")
            # if password == j:
            #     print("Verified! Access granted")
            # else:
            #     print("Access Denied")


@app.get("/root")
async def root():
    return("this is first data")