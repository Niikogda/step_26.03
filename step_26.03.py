
begin = int(input("enter the first number: "))
end = int(input("enter the last number: "))

for i in range(begin, end+1):
    print("all numbers: ", i)

for i in range(end, begin-1, -1):
    print("all numbers in back order: ", i)

for i in range(begin, end+1):
    if i %7 == 0:
        print("all numbers are multiples of seven: ", i)
count = 0
for i in range(begin, end+1):
    if i % 5 == 0:
        count += 1
print("amount of numbers multiples of five: ", count)