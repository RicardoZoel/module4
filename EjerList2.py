theList=[]
def addnumber():
    global theList
    num=int(input("Input a number "))
    theList.append(num)


def addnumberpos(pos,num):
    global theList
    if pos <= len(theList):
        theList.insert(pos,num)
    else:
        print("The index is out")


def delLast():
    global theList
    if len(theList)>0:
        return True
    return False


def delPos():
    global theList
    pos=int(input("Input a position "))
    if pos <= len(theList):
        return True
    else:
        return False


def countNumb():
    global theList
    num=int(input("Input a number "))
    return num


def posNumber():

    global theList
    num=int(input("Input a number "))
    pos=0
    for elem in range(0,theList.count(num)):
        index = theList.index(num,pos)
        print(index,end=" ")
        pos=index+1
    print()


while True:
    print("MENU")
    print("-------------------")
    print("1.- Add a number to the list")
    print("2.- Add a number in a position in the list")
    print("3.- Show the length of the list")
    print("4.- Delete the last number in the list")
    print("5.- Delete a number in the list")
    print("6.- Count numbers")
    print("7.- Positions of a numbers")
    print("8.- Show the list")
    print("9.- Exit")

    option = int(input("Choose an optione "))
    if option==1:
        addnumber()
    elif option==2:
        num=int(input("Input a number "))
        pos=int(input("Input a position "))
        addnumberpos(pos,num)
    elif option==3:
        print("the length of the list is: ",len(theList))
    elif option==4:
        if delLast():
            print("The last element is ", theList.pop(len(theList)-1)) 
    elif option==5:
        if delPos():
            print("Deleting the element: ", theList.pop(pos))
        else:
            print("The index is out")
    elif option==6:
        num = countNumb()
        print("the ocurrences of the number ",num," is ", theList.count(num))
    elif option==7:
        posNumber()
    elif option==8:
        for elem in theList:
            print(elem,end=" ")
        print()
    elif option==9:
        break


