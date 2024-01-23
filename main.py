import getpass

database = {'abena': '2345', 'Lena':'iwantto', 'Adlai':'ishetheone'}

username = input("Please enter your username: ")
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    for j in database.values():
        if username == i:
            while password != database.get(i):
                password = getpass.getpass("Please re-enter password: ")
                break
            print("Verified! Access Granted!")
            # if password == j:
            #     print("Verified! Access granted")
            # else:
            #     print("Access Denied")