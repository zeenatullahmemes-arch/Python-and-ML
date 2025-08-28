# # #  args operator is used to pass arguments to a function how many arguments we want
# # # used to make a function flexible

# # def add(*args):
# #     Total=0
# #     for i in args:
# #         Total += i
# #     return Total

# # print(add(1,2,3))  


# # def string(*args):
# #     output=[]
# #     for i in args:
# #         output.append(i[0][0])
# #     return output


# # print(string("apple","bannana","pear")) 

# # # args wth normal parameter
# # def mulitply(num1,num2,*args):
# #     total=1
# #     for i in args:
# #         total *= i
# #     return total 

# # print(mulitply(2,2,3))   


# # def mulitply(*args):
# #     total=1
# #     for i in args:
# #         total *= i
# #     return total


# # numbers=[1,2,3,4]
# # print(mulitply(*numbers)) # to unpack the list and pass it as an argument

# def fruits(*args):
#     output=[]
#     for i in args:
#         output.append(i[0][0])
#     return output

# # fruits_list=["apple","banana"]  
# # print(fruits(*fruits_list))   # used to unpack

# # def to_power(num,*args):
# #     if args:
# #         return [i**num for i in args]
# #     else:
# #         return "you did not pass anything"

# # num=[1,2,3]  
# # print(to_power(2,*num))


# def kwargs_Example(n,**kwargs):
#     print(f"your name is {n}")

#     for k,v in kwargs.items():
#       print (f" the key is {k} and value is {v}")
    
# d={"name":"zeenat Ullah","age":12}
# print(kwargs_Example("ali",**d))    

# # important to know
# # padk parameter args dafulat  parameter and kwargs
# def exam(name,*args,age=35,**kwargs):
#    print(f"your name is {name}")
#    total=0
#    for i in args:
#       total +=i
      
#    print(f"total is {total}")  
#    print(f"your age is {age}")  
#    for k,v in kwargs.items():
#       print(f"the key is {k} and value {v}") 

# numbers=[1,2,3,4]
# students_info={"n":"zeenat Ullah","A":34}
# print(exam("zeenat Ullah",*numbers,**students_info))

# # function to return the reverse of the string
# def func(l,**kwargs):
#    if kwargs.get("reverse_true")==True:
#       return [name[::-1].title() for name in l]
#    else:
#       return [name.title() for name in l]
   
# names=["fawad", "ali"]  
# print(func(names,reverse_true=True)) 


def arg(*args):
    total=0
    for i in args:
        total+=i
    return f"total is equal to {total}"

numbers=[1,2,3,4,5]
print(arg(*numbers))
    
      
   
    



