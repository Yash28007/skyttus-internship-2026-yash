age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")

color = input("Enter light color: ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

balance = int(input("Enter balance: "))
withdraw = int(input("Enter withdrawal amount: "))
if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

n = int(input("Enter number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
if low <= n <= high:
    print("Number is within range")
else:
    print("Number is outside range")

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100 * 1 + (units - 100) * 2
else:
    bill = 100 * 1 + 100 * 2 + (units - 200) * 3
print("Electricity bill =", bill)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+ - * /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operation")

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
