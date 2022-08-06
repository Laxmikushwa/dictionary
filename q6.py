# Write a program to remove duplicate keys.

dic={'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
}
e={}
for i in dic:
    if i not in e.keys():
        e[i]=dic[i]
print(e)