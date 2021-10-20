var = 1
def nameOfTheFunction(arg1="Default1",arg2="Default2"):
    print("Hello!!")
    print(arg1)
    print(arg2)
    global var
    var = 2
print(var)
nameOfTheFunction()
print(var)