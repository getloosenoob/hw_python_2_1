HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы"""

tasks = []

stop = False

while not stop:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        stop = True
    else:
        print("Неизвестная команда")
        print("До свидания!")
        stop = True