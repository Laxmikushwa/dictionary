# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
user=input("enter the user=")
e={}
for i in user:
    count=user.count(i)
    if i not in e.keys():
        e[i]=count
print(e)
