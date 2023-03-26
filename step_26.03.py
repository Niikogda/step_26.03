begin=int(input("enter first number: "))
end=int(input("enter second number: "))
if begin>end:
    begin, end = end, begin
for i in range(end, begin-1, -1):
    print(i)

    