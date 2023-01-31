a = int(input("Введите Число: "))
b = int(input("Введите Число: "))
simvol = input("Введите символ: ")
result = 0

if simvol == "+":
    result = a+b
    print(result)
elif simvol == "-":
    result = a-b
    print(result)
elif simvol == "*":
    result = a*b
    print(result)
elif simvol == "/":
    result = a/b
    print(result)

#