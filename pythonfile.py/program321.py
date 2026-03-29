User_Name = input("Enter your user name :")
password = input("ENter your password:")

if User_Name == "admin" and password == "password":
    
    print("Login successfully")

else:
    if User_Name != "admin":
        print("wrong User_Name")
    else:
        print("Wrong password")    



