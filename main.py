# in this project, i will create a task list, where we can add, delete and organize day-to-day tasks.
import aesthetics as ae, aid, os
from time import sleep

list_of_tasks = []

while True:
    # initial screen:
    if len(list_of_tasks) == 0:
        os.system('cls')
        aid.initial_screen()
        Answer = aid.validation()
        if Answer == 1:
            os.system('cls')
            aid.initial_screen()
            tarefa = aid.add(list_of_tasks)
            list_of_tasks.append(tarefa)
            os.system('cls')
            aid.initial_screen()
            print(ae.colors('Task added successfully', 'azul claro'))
            sleep(2)
            os.system('cls')
        else:
            print('Closing Program...')
            sleep(2)
            break

    #Viewing List:
    aid.list(list_of_tasks)

    #Validate Response:
    Answer_2 = aid.validation_2()

    #Add task:
    if Answer_2 == 1:
        os.system('cls')
        aid.list(list_of_tasks)
        tarefa = aid.add(list_of_tasks)
        list_of_tasks.append(tarefa)
        os.system('cls')
        aid.list(list_of_tasks)
        print(ae.colors('Task added successfully', 'azul claro'))
        sleep(2)

    #Remove task:
    elif Answer_2 == 2:
        os.system('cls')
        aid.list(list_of_tasks)
        list_of_tasks, item_removed = aid.remove(list_of_tasks)
        os.system('cls')
        aid.list(list_of_tasks)
        print(f'Task {ae.colors(f'{item_removed}', 'vermelho')} successfully removed')
        sleep(2)

    #Close the program:
    elif Answer_2 == 3:
        print('Closing Program...')
        sleep(2)
        break
