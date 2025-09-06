#numbers = [10, 20, 30, 40, 50]
#names = [ "Jami", "Ali", "Sara"]
#print(numbers[0])
#print(numbers[2])
#print(names[1])
#numbers = [5, 10, 15, 20]
#numbers[1] = 99
#print(numbers)
#names = ["Jami", "Ali", "Sara"]
#names[2] = "Omid"
#print(names)
#fruits = ["apple", "banana", "cherry", "date"]
#fruits[0] = "orange"
#fruits[3] = "grape"
#print(fruits)
#numbers = [10, 20, 30]
#numbers.append(40)
#print(numbers)
#names = ["Jami", "Ali", "Sara"]
#names.insert(1, "Omid")
#print(names)
#fruits = ["apple", "banana", "cherry"]
#fruits.remove("banana")
#print(fruits)
#numbers = [10, 20, 30, 40]
#numbers.pop(2)
#print(numbers)
#numbers = [1, 2, 3]
#numbers.pop()
#print(numbers)
#numbers = [10, 20, 30, 40]
#print(len(numbers))
#nums = [5, 2, 9, 1]
#nums.sort()
#print(nums)
#nums = [1, 2, 3, 4]
#nums.reverse()
#print(nums)
#fruits = ["apple", "banana", "apple", "cherry"]
#print(fruits.count("apple"))
#names = ["Jami", "Ali", "Sara"]
#print(names.index("Ali")j)
numbers = [15, 2, 30, 7, 25]

print("لیست اصلی:", numbers)

# مرتب‌سازی از کوچک به بزرگ
numbers.sort()
print("مرتب از کوچک به بزرگ:", numbers)

# مرتب‌سازی از بزرگ به کوچک
numbers.sort(reverse=True)
print("مرتب از بزرگ به کوچک:", numbers)

# فقط برعکس کردن لیست (بدون مرتب‌سازی)
numbers = [15, 2, 30, 7, 25]  # دوباره لیست اصلی
numbers.reverse()
print("فقط برعکس کردن لیست:", numbers)

