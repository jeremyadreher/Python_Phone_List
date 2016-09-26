try:
    from myList import *
except:
    myList = ["red", "green", "blue"]


def printColors():
    for color in myList:
        print(color)

def saveList():
    filename = open("myList.py", "w")
    filename.write("myList = " + str(myList))
    filename.close()

def main():
    color = input("Enter a color to add: ")
    myList.append(color)
    saveList()
    print("Colors in the list are:")
    printColors()

main()

    
