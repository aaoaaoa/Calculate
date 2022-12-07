n1 = int(input("Введите 1-ое число "))
n2 = int(input("Введите 2-ое число "))
sign = input("Введите знак операции ")
res=0

if sign == "+":
  res = n1+n2
elif sign == "-":
  res = n1-n2
elif sign == "/":
  res = n1/n2
elif sign == "*":
  res = n1*n2
elif sign == "**":
  res = n1**n2
else:
  print("Неверный знак")

print("Результат = ",res)
