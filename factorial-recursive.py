
#Calculating Factorial with Recursive Function
__Author__="Aslan"


def fact(num):

    if(isinstance(num,int)==False):
        return print("Invalid Value Error")

    elif (isinstance(num, int) == True):
        if(num==0):
            return 1
        return num*fact(num-1)

    else:
        return print("There is an error.")
print(fact((int(input("Type a number to calculate factorial value : ")))))
