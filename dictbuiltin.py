# Access & Information Functions

'''get(key, default):
    Returns value of key, else returns default.

keys():
    Returns all keys (view object).

values():
    Returns all values (view object).

items():
    Returns all key-value pairs as tuples (view object).

copy():
    Returns a shallow copy of dictionary.

setdefault(key, default):
    If key exists, returns its value; else inserts key: default and returns default.'''

# Update & Modification Functions

'''update(other_dict):
    Updates dictionary with another dictionary or key-value pairs.

pop(key, default):
    Removes and returns value of key. If not found, returns default.

popitem():
    Removes and returns the last inserted key-value pair (LIFO order).

clear():
    Removes all items, making dictionary empty.'''

#Class Method

'''dict.fromkeys(seq, value):
    Creates a new dictionary with keys from seq, all having the same value.'''
    
    
#write internal code fromkeys() function
'''def fromkeys():
    d={"name":"aravind","age":21,"place":"chittoor"}
    res=dict.fromkeys(d,0)
    print(res)
fromkeys()'''
