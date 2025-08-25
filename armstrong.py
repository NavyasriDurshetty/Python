num=153
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp=temp//10
if num==sum:
    print("it is armstrong number",num)
else:
    print("it is not armstrong number",num)   
