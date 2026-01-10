a = 17
b = 5
remainder = a % b
print("Remainder of", a, "and", b, "is", remainder)

num = 8
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

x = 15
y = 20
if x > y:
    print("Larger number is", x)
else:
    print("Larger number is", y)

n = 4
square = n ** 2
cube = n ** 3
print("Square of", n, "is", square)
print("Cube of", n, "is", cube)

p = 12
q = 12
print("Numbers are equal:", p == q)

m = 5
n1 = -3
print(m > 0 and n1 > 0)

f = 7.89
i = int(f)
print("Float:", f, "converted to integer:", i)

s = "6"
num_s = int(s) * 10
print("String", s, "multiplied by 10 is", num_s)

a1 = 8
b1 = 12
c1 = 5
print("Result of condition check:", (a1 > 5 and b1 < 15) or (c1 == 5))

dividend = 29
divisor = 4
quotient = dividend // divisor
remainder = dividend % divisor
print("Quotient:", quotient)
print("Remainder:", remainder)
