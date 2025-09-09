#ASSESMENT-3
#TASK1
print("task 1 \n")

def factorial(n):
    if n<0:
        return "not  valid because it is a negative no. "
    result=1
    for i in range(1, n + 1):
        result *= i
    return result

num=int(input("enter the no."))
print(f"the factor of {num} is {factorial(num)}")



#TASK2
print("\n task 2 \n")


import math
num=float(input("enter a no."))

sqrt_val=math.sqrt(num)

if num>0:
    log_val=math.log(num)
else:
    log_val="not defined"

sine_val=math.sin(num)

print("squareroot :",sqrt_val)
print("logarithm :",log_val)
print("sine :",sine_val)
