# Write a program to print the top 3 highest values of a given dictio
my_dict = {
'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
e=[]
for i in my_dict:
    e.append(my_dict[i])
e.sort(reverse=True)
print(e[0:3:1])
