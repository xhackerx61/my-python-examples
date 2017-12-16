file = open("keys.txt", "r+")
myList = file.read().split(",")
for i in myList:
    for j in myList:
        makeComb = i+":"+j
        print(makeComb) 
        #if u want,u can add the results to a file
        
