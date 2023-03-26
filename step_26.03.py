begin=int(input("enter the first number: "))
end=int(input("enter the last number: "))
for i in range(begin, end+1):
    if i %3 == 0:
        i=(i, "= fizz")
        print(i)
for i in range(begin, end+1):
    if i %5 == 0:
        i=(i, "= Buzz")
        print(i)
for i in range(begin, end+1):
    if i %15 == 0:
        i=(i, "= fizzBuzz")
        print(i)
for i in range(begin, end+1):
    if i %3 != 0 and i %5 !=0 and i %15 !=0:
        print(i)