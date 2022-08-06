# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
e={}
for i in dic1 :
    if i not in dic2 :
        e[i]=dic1[i]
    else :
        e[i]=(dic1[i]+dic2[i])
for x in dic2 :
    if x not in e :
        e[x]=dic2[x]
    else:
        e[x]=e[x]+dic2[x]
for b in dic3:
    if b not in e:
        e[b]=dic3[b]
    else:
        e[b]=e[b]+dic3[b]
print(e)


# 19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# e={}
# for i in d1 :
#   if i not in d2 :
#     e[i]=d1[i]
#   else :
#     e[i]=(d1[i]+d2[i])
# for x in d2 :
#   if x not in e :
#     e[x]=d2[x]
# print(e)
