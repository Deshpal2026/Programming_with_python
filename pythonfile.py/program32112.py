def Calculate_EvenNumber(a,b):
    EvenNumber = []
    for i in range(a,b+1):
        if i % 2 == 0:
            EvenNumber.append(i)
    return EvenNumber
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
number = Calculate_EvenNumber(a, b)
print(number)       