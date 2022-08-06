# # Write a program to print the top 3 highest values of a given dictionary.

# my_dict = {
# 'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# e=[]
# for i in my_dict:
#     e.append(my_dict[i])
# e.sort(reverse=True)
# a=e[0:3:1]
# b=[]
# for k,v in my_dict.items():
#     for i in a:
#         if v==i:
#             b.append(k)
# print(b)
# # print(a)


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
a=e[0:3:1]
b=[]
for k,v in my_dict.items(): # ye hamara key aur value leke aayega
    for i in a: # ye loop hum 3 hieghtest value ko leke aa raha hai 
        if v==i: # yanha par compare kar rahe hai 
            b.append(k) # agar condition true ho to b list me append kr de k ko 
print(b)