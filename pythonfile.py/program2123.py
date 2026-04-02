salary = int(input("Enter salary : "))
if salary < 30000 :
    final_tax = (salary *5)//100
    print(final_tax)
elif salary > 30000 and salary < 70000:
    final_tax = (salary*15)//100
    print( final_tax)
elif salary > 70000:
    final_tax = (salary*25)//100
    print( final_tax)
else:
    print("no tax")                