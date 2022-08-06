# # Write a program to sort a dictionary in ascending or descending according to its values .
dic={
    'bijender':45,
    'deepak':60,
    'param':20,
    'anjili':30,
    'roshini':50
}
a=[]
for i in dic.values():
    a.append(i)
# a.sort(reverse=True)
a.sort(reverse=False)
# print(a)
d={}
for z in a: 
    for k,v in dic.items():
        if v==z:
            d[k]=v
print(d)
