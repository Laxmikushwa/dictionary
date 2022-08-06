# Take a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
li=[ 
{"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
e=[]
for i in li:
    for j in i:
        if i[j] not in e:
            e.append(i[j])
print(e)
