todo = []

while True:
    ch = int(input("1 add task\n2 delete task\n3 view task\n4 exit\n enter choice : "))
    
    if ch == 1:
        task = input("Enter task: ")
        todo.append(task)
        print("Task added successfully") 
    elif ch == 2:
        if len(todo) == 0:
            print("No tasks to delete")
        else:
            task = input("Enter task to delete: ")
            if task in todo:
                todo.remove(task)
                print("Task deleted successfully")
            else:
                print("Task not found")   
    elif ch == 3:
        if len(todo) == 0:
            print("No tasks to view")
        else:
            print("Tasks:")
            for task in todo:
                print(task)
            print() 
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Invalid option")
    