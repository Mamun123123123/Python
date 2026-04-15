# for values
# for i in a:
#     print(i)
#     # for index
# for i in range(len(a)):
#     print(i)     

# help(list)

# a = [-1,2,2,-3,4,5]

# print(a.count(2))
# a.append(30)
# a.insert(2,20)
# print(a)

# a = [-1,2,2,-3,4,5]
# positive = []
# negative = []
# for i in a:
#     if i>=0:
#         positive.append(i)
#     else:
#         negative.append(i)

# print(positive)
# print(negative)

# a = [2,4]
# sum = 0
# for i in a:
#      sum = sum + i
# mean = sum / len(a)
# print(mean)     

# a = [2,10,5,8]
# max = a[0]
# for i in a:
#     if i> max:
#         max = i
# print(max)    

a = [2,10,5,8]
max = a[0]
second_max = a[1]
for i in a:
    if i> max:
        second_max = max
        max = i
    elif i>second_max and max != i:
        second_max = i
print(second_max)    


