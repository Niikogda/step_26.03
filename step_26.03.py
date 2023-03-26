begin=int(input("enter begining: "))
end=int(input("enter ending: "))
if begin>end:
    begin, end = end, begin
else:
     begin, end =  begin, end
for i in range(begin, end+1):
    if i %7 == 0:
        print(i)