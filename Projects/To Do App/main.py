def task():
    tasks = []
    print("----WELCOME----")

    taskNum = int(input("Enter how many tasks you want to add : ").strip())

    for i in range(1, taskNum + 1):
        task_item = input(f"Enter task {i} : ").strip()
        if task_item:          # avoids empty tasks
            tasks.append(task_item)

    print(f"\nTasks are successfully added\n{tasks}")

    while True:
        print(
            "\n1. Add",
            "\n2. Update",
            "\n3. Delete",
            "\n4. View all tasks",
            "\n5. Stop / Exit"
        )

        user_choice = int(input("\nEnter Your Choice : ").strip())

        if user_choice == 1:
            new_task = input("\nEnter the new task : ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Your task '{new_task}' is added successfully")

        elif user_choice == 2:
            task_to_update = input("\nEnter the task that you need to update : ").strip()

            if task_to_update in tasks:
                updated_task = input("\nEnter the new task : ").strip()
                if updated_task:
                    idx = tasks.index(task_to_update)
                    tasks[idx] = updated_task
                    print(f"Your task '{updated_task}' is updated successfully")
            else:
                print(f"'{task_to_update}' is an invalid task")

        elif user_choice == 3:
            task_to_delete = input("\nEnter the task you need to delete : ").strip()

            if task_to_delete in tasks:
                tasks.remove(task_to_delete)
                print(f"Task '{task_to_delete}' is deleted successfully")
            else:
                print(f"'{task_to_delete}' is an invalid task")

        elif user_choice == 4:
            if tasks:
                print("\nYour tasks are:")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
            else:
                print("No tasks available")

        elif user_choice == 5:
            print("Thanks for using this To-Do App")
            break

        else:
            print(f"{user_choice} is an invalid input")


task()