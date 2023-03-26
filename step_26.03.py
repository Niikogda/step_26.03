begin=int(input("enter first number: "))
end=int(input("enter second number: "))

for i in range(begin, end+1):
    if i %2 != 0:
        print(i)
    