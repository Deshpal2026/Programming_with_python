while True:
  User_input = input("Enter a number or quit :")
  if User_input == "quit":
     break

  try:

     n = int(User_input)
     if n>0:
         print("Positive")
     elif n<0:
        print("Negative")
     else:
        print("0")
  except:
    print("Invalid input, Again try")                



