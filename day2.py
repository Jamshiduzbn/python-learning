# age = int(input("Enter your age: ")) 
#if age >=18:
#    print("You are an adult.")
#else:
#    print("You are not an adult.")
#    a = 10
#    b = 3
#   print("a + b =", a + b) 
#    print("a - b =", a - b)
#   print("a * b =", a * b)
#   print("a / b =", a / b)
#   print("a // b =", a // b)
#   print("a % b =", a % b)
#   print("a ** b =", a ** b)
#    age = 20
#   if age >=18:
#        print("You are adult")
#    else:
#        print("You are not an adult")
#    age = 13
#    if age >= 18:
#        print("adult")
#    elif age >=13:
#        print("Teenager")
#    else:
#        print("Child")
#
#n  = int(input("Enter a number: "))
# if n % 2 == 0:
    print("even")
#else:
#    print("odd")
#
#


#n = int(input("Enter a number: "))

#if n % 2 == 0:
  #  print("Even")
#else:
#   print("Odd")


a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Unknown operator")