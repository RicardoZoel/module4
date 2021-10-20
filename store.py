quantProducts = {1:10, 2:4, 3:0, 4:9}
priceProducts = {1: 9.99, 2:19.99, 3:14.99, 4:4.99 }
cash=129.9
def getPriceProduct(code):
    return priceProducts[code]
def getQuanityProduct(code): 
    return quantProducts[code]
def getDetailProduct(code):
    return (priceProducts[code]," , ",quantProducts[code])
def getCash():
    return cash
def setPriceProduct(code, price):
    quantProducts[code]=price
def saleProduct(code):
    if code in quantProducts:
        return True
    else:
        return False
def replaceProduct(code, quantity):
    global cash
    if (cash-(((priceProducts[code]*quantity)/100)*80))>=0:
        cash-=(((priceProducts[code]*quantity)/100)*80)
        return True
    else:
        return False
def getFullStock():
    print("Current store status")
    print("=======================")
    print("Product detail:")
    print(" [Code – Units – Price]")
    for elem in quantProducts:
        print("[",elem," – ",quantProducts[elem]," – ",priceProducts[elem],"]")
    print("Cash: ",getCash(),"€")

def getcode():
    code=int(input("Enter product code: "))
    if code in quantProducts:
        return code
    else:
        print("Error, item does not exist or is out of stock!.")
        return False


while(True):
    print("1.- Show full store detail")
    print("2.- Sales")
    print("3.- Replace")
    print("4.- Change price of product")
    print("5.- Exit")
    option=int(input("Input a optión "))
    if option==1:
        getFullStock()
    elif option==2:
        code=int(input("Enter product code: "))
        if saleProduct(code):
            print("Successful sale!")
        else:
            print("Error, item does not exist or is out of stock!.")
    elif option==3:
        code=getcode()
        if code==False: 
            continue
        quantity=int(input("Units to replace: "))
        if replaceProduct(code,quantity):
            print("Correct replacement!")
        else:
            print("There is no cash in the box to replace!")

    elif option==4:
        code=getcode()
        if code==False: 
            continue
        quantity=int(input("New price for product: "))
        setPriceProduct(code,quantity)
        print("Updated price!")
    elif option==5:
        break
    else:
        continue
