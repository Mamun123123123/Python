# a = range(1,21,2)
# for i in a:
#     print(i)

# for i in range(10):
#     print(i)    

# for i in range(16,0,-1):
#             print(i)

# for i in range(-1,-15,-1):
#         print(i)            

# for i in range(10,101,10):
#     print(i)

# n = int(input("Enter your number "))
# for i in range(n,(n*10)+1,n):
#     print(i)

# str = "Abdullah Al Mamun"
# for i in range(len(str)):
#     print(str[i])
# for i in str:
    # print(i)   
# for i in range(1,100,1):
#     if i == 10:
#         break
#     else:
#         print(i) 

# for i in range(1,100,1):
#     if i == 10:
#         continue
#     else:
#         print(i) 
# n = int(input("Enter your number "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
# n = int(input("Enter your number "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i

# print(f"your Sum is {sum}")

# n = int(input("Enter your number "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(f"your factorial is {fact}")

n = int(input("Enter your number "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"Your Even is {even}")
print(f"your Odd is  {odd}")