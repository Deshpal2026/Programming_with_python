User_Name = input("Enter your user name :")
password = input("Enter your password :")
if User_Name == "admin" and password == "1234":
    print("Login successfull!")
elif User_Name != "admin" :
    print("Invalid username!")  
elif password !="1234":
    print("Invalid password!")
    
