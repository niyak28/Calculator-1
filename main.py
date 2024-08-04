import graphics
print("hello world")

cont = ("y")
num1 = int(input("num 1? "))

while cont==str("y"):
  num2 = int(input("num2? "))

  print("1=*")
  print("2=/")
  print("3=-")
  print("4=+")
  op = str(input("operation? "))

  if op == "1":
    ans = num1 * num2
  elif op=="2":
    ans = num1 / num2
  elif op=="3":
    ans = num1 - num2
  elif op=="4":
    ans = num1 + num2
  # make an exponent calculator #
  elif op == "5":
    ans = num1 ** num2
  num1 = ans
  print(str(ans))



cont = ("continue? y or n ")