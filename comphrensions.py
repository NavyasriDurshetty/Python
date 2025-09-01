#smallest and second smallest number in a list
'''ip=[8,9,3,4,5,6]
smallest=ip[0]
second_smallest=ip[0]
for x in ip:
    if x<smallest:
        second_smallest=smallest
        smallest=x
    elif x<second_smallest and x!=smallest:
        second_smallest=x
print("smallest number is:",smallest) 
print("second smallest number is:",second_smallest)  '''    

ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
for i in ip:
    if i.endswith(('i','a')):
      print(("female",i))
    elif i.endswith(('n','r','h')):
       print(("male",i))
     
        