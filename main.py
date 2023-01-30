a = int(input("Введите Число: "))
b = int(input("Введите Число: "))
simvol = input("Введите символ: ")
resault = 0

if simvol == "+":
    resault = a+b
    print(resault)
elif simvol == "-":
    resault = a-b
    print(resault)
elif simvol == "*":
    resault = a*b
    print(resault)
