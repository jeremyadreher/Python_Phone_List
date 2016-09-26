from tkinter import *

try:
    from phoneList import *
except:
    phoneList = [
        ['Meyers, Chris', '343-4349'],
        ['Smith, Robert', '689-1234'],
        ['Jones, Janet', '483-5432'],
        ['Barnhart, Ralph', '683-2341'],
        ['Nelson, Eric', '485=2689'],
        ['Prefect, Ford', '987-6543'],
        ['Zigler, Mary', '567-8901'],
        ['Smith, Bob', '689-1234'],
        ]

def whichSelected():
    print (select.curselection(), len(phoneList))
    return int(select.curselection()[0])
    
def addEntry():
    phoneList.append([nameVar.get(), phoneVar.get()])
    setSelect()

def updateEntry():
    phoneList[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect()

def deleteEntry():
    del phoneList[whichSelected()]
    setSelect()

def loadEntry():
    name, phone = phoneList[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

def saveList():
    filename = open('phoneList.py', 'w')
    filename.write('phoneList = ' + str(phoneList))
    filename.close()
            
def makeWindow():
    global nameVar, phoneVar, select
    root = Tk()
    root.title('Python Phone List')

    # Name & Phone Entry
    frame1 = Frame(root) 
    frame1.pack()

    Label(frame1, text = 'Name').grid(row = 0, column = 0, sticky = W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable = nameVar)
    name.grid(row = 0, column = 1, sticky = W)

    Label(frame1, text = 'Phone').grid(row = 1, column = 0, sticky = W)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable = phoneVar)
    phone.grid(row = 1, column = 1, sticky = W)

    # Row of buttons
    frame2 = Frame(root) 
    frame2.pack()
    b1 = Button(frame2, text = 'Add ', command = addEntry)
    b2 = Button(frame2, text = 'Update', command = updateEntry)
    b3 = Button(frame2, text = 'Delete', command = deleteEntry)
    b4 = Button(frame2, text = 'Load', command = loadEntry)
    b5 = Button(frame2, text = 'Save', command = saveList)
    b1.pack(side = LEFT)
    b2.pack(side = LEFT)
    b3.pack(side = LEFT)
    b4.pack(side = LEFT)
    b5.pack(side = LEFT)

    # List of names
    frame3 = Frame(root)
    frame3.pack()
    scroll = Scrollbar(frame3, orient = VERTICAL)
    select = Listbox(frame3, yscrollcommand = scroll.set, height = 6)
    select.insert(END, phoneList)
    scroll.config(command = select.yview)
    scroll.pack(side = RIGHT, fill = Y)
    select.pack(side = LEFT, fill = BOTH, expand = 1)
    return root

def setSelect():
    phoneList.sort()
    select.delete(0, END)
    for name, phone in phoneList:
        select.insert(END, name)
        

root = makeWindow()
setSelect()
root.mainloop()
