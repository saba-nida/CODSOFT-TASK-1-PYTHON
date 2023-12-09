print("-------------------------TO-DO LIST------------------------------")
print("")
list=[]

def print_todo_list():
    if list== []:
        print("you dont have any tasks in the to-do list")
    else:
        print("")
        print("--------------------YOUR TO DO LIST--------------------------")
        print("")
        for i in list:
            print(i)  
        print("")          

def add_task(task):
    list.append(task)
    print("the task has been Added")

def remove_task(task_number):
    if task_number<=len(list):
        list.pop(task_number-1)
        print("the task has been removed")
    else:
        print("invalid task number")

while True:
    print("Enter 1 to display your to-do list")
    print("Enter 2 to add tasks to your to-do list")
    print("Enter 3 to remove tasks from your to-do list")
    print("Enter 4 to exit ")
    select = (input("please enter the selected number :"))


    if select == '1':
        print_todo_list()
    elif select== '2':
        task=input(" enter the task you wanna add: ")
        add_task(task)
    elif select == "3":
        task_number= int(input("enter the task number you wanna remove: "))
        remove_task(task_number)
    elif select=="4":
        print("exiting ")
        break
    else:
        print("invalid number")