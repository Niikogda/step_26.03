s=13
e=33
begin=end=-1
begin=int(input("enter begining: "))
end=int(input("enter ending: "))
if begin > end:
    begin, end = end, begin
else: 
     begin, end =  begin, end
while begin < s or begin > e:
    begin=int(input("enter begining: "))
while end < s or end > e:
    end=int(input("enter ending: "))
for i in range(begin, end+1):
    if i %2 != 0:
        print(i)
