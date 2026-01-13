while True:
    print("\nMENU")
    print("1. Print numbers from 1 to 10")
    print("2. Multiplication table")
    print("3. Factorial")
    print("4. Fibonacci series")
    print("5. Prime check")
    print("6. Reverse a number")
    print("7. Count digits")
    print("8. Sum of even numbers (1-100)")
    print("9. Pyramid pattern")
    print("10. Divisors of a number")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(1, 11):
            print(i)

    elif choice == 2:
        n = int(input("Enter number: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)

    elif choice == 3:
        n = int(input("Enter number: "))
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial =", fact)

    elif choice == 4:
        n = int(input("Enter N: "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif choice == 5:
        n = int(input("Enter number: "))
        if n <= 1:
            print("Not Prime")
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    print("Not Prime")
                    break
            else:
                print("Prime")

    elif choice == 6:
        n = int(input("Enter number: "))
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        print("Reversed number =", rev)

    elif choice == 7:
        n = int(input("Enter number: "))
        count = 0
        while n > 0:
            count += 1
            n //= 10
        print("Number of digits =", count)

    elif choice == 8:
        total = 0
        for i in range(2, 101, 2):
            total += i
        print("Sum of even numbers =", total)

    elif choice == 9:
        rows = int(input("Enter rows: "))
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2*i - 1))

    elif choice == 10:
        n = int(input("Enter number: "))
        print("Divisors:")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=" ")
        print()

    elif choice == 0:
        print("Exited")
        break

    else:
        print("Invalid choice")
