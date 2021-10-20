
def factorial(num):
    num2=num
    result=1
    for elem in range(0,num):
        result*=num2
        num2-=1
    return result

num=int(input("Input a number "))

print(factorial(num))