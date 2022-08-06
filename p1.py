# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

# fruit = {}

# def addone(index):
#  if index in fruit:
#   fruit[index] += 1
#  else:
#   fruit[index] = 1
  
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print(len(fruit))
# print(fruit)

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details["Student"]))

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#  sum += my_dict[k]

# print(sum)
# print(my_dict)


# d = dict(foo=100, bar=200, baz=300)
# print(d)
# d=dict()
# print(d)
list1 = [2, -7, 5, -64, -14]
# # Output: pos = 2, neg = 3
# i=0
# count=0
# while i<len(list1):
#     if list1[i]>=0:
#         print(list1[i],"positive")
#     else:
#         print(list1[i],"negative")
#     i+=1

# list1= [1,2,3,5,-4,-6]
def list1():
    list1 = [2, -7, 5, -64, -14]
    pos = 0
    neg = 0
    i = 0 
    while i < len(list1):
        if list1[i] > 0 :
            pos+=1
        else:
            neg+=1
        i+=1
    print("pos=",pos)
    print('neg=',neg)
list1()