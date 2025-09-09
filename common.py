# Common Built-in Functions (String | List | Tuple)
'''
len() → Returns number of elements.
Syntax: len(string) | len(list) | len(tuple)

max() → Returns largest element.
Syntax: max(string) | max(list) | max(tuple)

min() → Returns smallest element.
Syntax: min(string) | min(list) | min(tuple)

sum() → Returns sum of numeric elements.
Syntax: sum(list) | sum(tuple) (not for string)

sorted() → Returns elements in ascending order as list.
Syntax: sorted(string) | sorted(list) | sorted(tuple)

any() → Returns True if any element is true.
Syntax: any(string) | any(list) | any(tuple)

all() → Returns True if all elements are true.
Syntax: all(string) | all(list) | all(tuple)

enumerate() → Returns index-value pairs as iterator.
Syntax: enumerate(string) | enumerate(list) | enumerate(tuple)

reversed() → Returns reverse iterator.
Syntax: reversed(string) | reversed(list) | reversed(tuple)

in / not in → Checks membership of element.
Syntax: element in string | element in list | element in tuple'''


#. write codes to find second largest and second smallest element in a list
'''l=[10,100,99,9,999]
min=l[0]
second_min=l[0]+1
for i in l:
    if i<min:
       min=i
    elif i<second_min:
        second_min=i
       
print(min) 
print(second_min)  '''