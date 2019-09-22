#tutorial source: https://www.youtube.com/watch?v=kB829ciAXo4

#unknown keyword arguments, unlabeled
#first item is labeled, but not the following items.
def person(name, *data):
    print(name)
    print(*data)
    print(data)
    
person('Bob', 30, 'New York', 2064055246)


print(60*'-')

#unknown keyward arguments, but labeled
#first item is labled, as is the rest.
def person(name, **data):
    print(name)
    
    for key, value in data.items():
        print(key, value)
    
person('Bob', 
       age = 30, 
       City='New York', 
       mobile = 2064055246)
