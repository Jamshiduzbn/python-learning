# Day 3 - Step 1
# چاپ اعداد 1 تا 5 با حلقه for

# for i in range(1, 6):
  #  print(i)
#names = ["Jami", "Ali", "Sara"]
#for name in names:
#    print(name)
#range(start, stop, step)
#for i in range(5):
#    print(i)
#for i in range(2, 6):
#    print(i)
#for i in range(0, 10, 2):
#    print(i)
#i = 1

#while i <= 5:
#    print(i)
#    i = i + 1   # هر بار 1 اضافه می‌کنیم
i = 5
#while i> 0:
#    print(i)
#    i = i - 1


#print("Boom!")
#for i in range(1, 10):
#    if i == 5:
#        break
#   print(1)

#for i in range(1, 10):
#    if i == 5:
#        break
#    print(i)

for i in range(1, 11):
    if i == 7:
        print("Found 7!")
        break
    print(i)

for i in range(1, 6):
    if i ==3:
        continue
    print(i)

i = 5
while i > 0:
    if i == 2:
        print("Skip 2")
        i -= 1
        continue
    print(i)
    i -= 1
