def Is_palindrom(text):
  text = text.lower()
  riverse_text = text[ :: -1]
  if text == riverse_text :
     print("It is pailindrom")
  else:
     print("It is not palindrom")
text = input("Enter a text : ")
Is_palindrom(text)