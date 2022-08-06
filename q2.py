# Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.
dict1={"name":"Raju", "marks":56}
user = input("enter key ____: ")
if user in dict1.keys():
    print('exist')
else:
    print('Not exist')