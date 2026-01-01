#----- STOCK -----#
product ={}

def addProduct(): #DONE
    code=input("Product's code: ")
    name=input("Product's name:")
    price=float(input("Product's price: "))

    product[code]= {"name":name, "price":price, "qty":0}

    addStock(code)

def addStock(code): #DONE
    qty=int(input("Units to add on stock: "))
    product[code]["qty"]+=qty
    salesMenu()

def reduceStock(code): #DONE
    qty=int(input("Units to subtract from stock: "))
    if((product[code]["qty"]-qty)<0):
        print("Invalid input. Stock quantity must not be less than 0.\n")
        salesMenu()
    product[code]["qty"]-=qty
    salesMenu()

#----- TASKS -----#
tasks={}
tasknum=0

def addTask():
    subject=input("Task description: ")
    assignTo=input("Assign to: ")
    assignFor=input("Client: ")

    tasks[tasknum]={"Task":subject, "Assignee":assignTo, "Client":assignFor}
    tasknum+=1
    #dueTo=input("Due to")#TODO STORE DATE

def showTasks():
    headers = []
    for task in tasks.values():
        for key in task:
            if key not in headers:
                headers.append(key)

    headers = ["TaskID"] + headers

    print(" | ".join(headers))
    print("-" * len(" | ".join(headers)))

    for task_id, task in tasks.items():
        row = [str(task_id)] + [str(task.get(h, "")) for h in headers[1:]]
        print(" | ".join(row))

def endTask():
    taskID = int(input("Input task ID you want to mark as completed: "))
    if taskID in tasks:
        #TODO MOVE TO COMPLETED
        del tasks[taskID]
    else:
        print(f"Task {taskID} does not exist")



#----- MAIN & USERS -----#
def main():
    login()
    menu()

def login():
    username = input("Input username: ")
    passwd = input(f"Input {username} password: ")
    
    #search credentials for log in
    
def addUser():
    user = input("User's name: ")
    passwd = input("User's password: ")

    #register info


#----- Menus -----#

def menu():
    userInput = input("---Main Menu---\n-- Sales/ Purchases Menu (1)\n-- Tasks Menu (2)\n-- Rest(3)\n-- Close Program (0)\n")

    if (userInput=="1"):
        salesMenu()
    elif (userInput=="2"):
        #TODO tasksMenu()
        print("TODO")
        menu()
    elif (userInput=="3"):
        #TODO restMenu()
        print("TODO")
        menu()
    else:
        print("Invalid Input")
        menu()

def salesMenu():
    option = input("---Sales Menu---\n\n1. Add Sale\n2. View Sales\n3. Add units\n4. Register new product\n0. Back to Main menu\n")

    if(option=="1"):
        itemCode=input("Input item's code: ")

        if itemCode not in product:
            print("Code not found!")
            salesMenu()
        
        reduceStock(itemCode)
    elif(option=="2"):
        print("TODO")
        menu()
        #TODO INPORT FROM JSON
    elif(option=="3"):
        itemCode=input("Input item's code: ")

        if itemCode not in product:
            print("Code not found!")
            salesMenu()
        
        addStock(itemCode)
    elif(option=="4"):
        addProduct()
    elif(option=="0"):
        menu()
    else:
        print("Invalid Input")
        salesMenu()

def tasksMenu():
    option = input("---Tasks Menu---\n\n1. Add Task\n2. View Tasks\n3. Close Task\n0. Back to Main menu\n")

    if(option=="1"):
        addTask()
    elif(option=="2"):
        showTasks()
    elif(option=="3"):
        endTask()
    elif(option=="0"):
        menu()
    else:
        print("Invalid Input")
        tasksMenu()


if __name__ == "__main__":
    main()
