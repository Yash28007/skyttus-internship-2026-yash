s = input("Enter a string: ")
print(len(s))

sentence = input("Enter a sentence: ")
print(sentence.lower())

text = input("Enter a string to replace spaces: ")
print(text.replace(" ", "_"))

s2 = input("Enter a string to get first and last character: ")
print(s2[0])
print(s2[-1])

s3 = input("Enter a string to reverse: ")
print(s3[::-1])

s4 = input("Enter a string: ")
letter = input("Enter a letter to count: ")
print(s4.count(letter))

sentence2 = input("Enter a sentence: ")
word = input("Enter a word to search: ")
print(word in sentence2)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

text2 = input("Enter a string with extra spaces: ")
print(text2.strip())

words = ["Python", "is", "awesome"]
print(" ".join(words))


movies = ["Sholay", "3 Idiots", "Lagaan", "Kabir Singh", "Bahubali"]
print(movies)

movies.append("RRR")
print(movies)

movies.pop(0)
print(movies)

numbers = [45, 12, 78, 34, 23]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(max(numbers))

list1 = ["Ram Charan", "Prabhas", "Hrithik Roshan"]
list2 = ["Ranbir Kapoor", "Tiger Shroff"]
merged_list = list1 + list2
print(merged_list)

print(merged_list[-1])

nested_list = [["RRR", "Ram Charan"], ["Bahubali", "Prabhas"], ["Kabir Singh", "Shahid Kapoor"]]
print(nested_list[1][1])

items = ["apple", "banana", "apple", "orange", "apple"]
print(items.count("apple"))


numbers = (10, 20, 30, 40, 50)
print(numbers)

print(numbers[2])

a, b, c, d, e = numbers
print(a, b, c, d, e)

fruits = {"apple", "banana", "mango", "orange", "grape"}
print(fruits)

fruits.add("pineapple")
print(fruits)

fruits.remove("banana")
print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))

print(set1.intersection(set2))

print(set1.issubset(set2))

duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(duplicate_list)
print(unique_set)
