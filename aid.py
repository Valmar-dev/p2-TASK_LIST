# This file will be used to create functions that will be used in the development of the project.
import aesthetics as ae, os
from time import sleep


#creating initial screen and firts options:
def initial_screen():
    ae.title(ae.colors('TASK LIST', 'amarelo'))
    print(ae.colors('No tasks at the moment', 'vermelho').center(50))
    print('-' * 50)
    print(ae.colors('[1]', 'azul claro'), ae.colors(' <Create a new list task>', 'amarelo'))
    print(ae.colors('[2]', 'azul claro'), ae.colors(' <Close the program>', 'amarelo'))
    print('-' * 50)


# creating validation of data of initial screen:
def validation():
    while True:
        try:
            answer_client = int(input(f'{ae.colors('Type [1] to create a new task list or [2] to close the program: ', 'amarelo')}'))
            if answer_client == 1 or answer_client == 2:
                return answer_client
            else:
                print(f'{ae.colors('Ops!, type only [1] or [2]', 'vermelho')}')
                sleep(2)
        except:
            print('Ops!, type only [1] or [2]')
            sleep(2)


# Adding new task:
def add(list):
    task = str(input(f'{ae.colors(f'Type the task <{len(list) + 1}>: ', 'amarelo')}'))
    return task


#Removing new task:
def remove(list):
    while True:
        try:
            item = int(input(f'{ae.colors('Which task will be removed?(Enter the position of the task)', 'amarelo')}'))
            if item <= len(list):
                item_removed = list[item - 1]
                list.pop(item - 1)
                return list, item_removed
            else:
                print(f'Position not found.')
        except:
            print(f'Position not found.')


# Creating the list:
def list(list):
    import os
    os.system('cls')
    ae.title(ae.colors('TASK LIST', 'amarelo'))
    for n, i in enumerate(list):
        print(ae.colors(f'<{n + 1}> - ', 'verde'), i)
    print('-' * 50)
    print(ae.colors('[1]', 'azul claro'), ae.colors('Add a new task', 'amarelo'))
    print(ae.colors('[2]', 'azul claro'), ae.colors('Delete a task', 'amarelo'))
    print(ae.colors('[3]', 'azul claro'), ae.colors('Close the program', 'amarelo'))
    print('-' * 50)


#General options data validation:
def validation_2():
    while True:
        try:
            answer_client_2 = int(input(f'{ae.colors('Choose one of the options above: ', 'amarelo')}'))
            if answer_client_2 == 1 or answer_client_2 == 2 or answer_client_2 == 3 or answer_client_2 == 4:
                return answer_client_2
            else:
                os.system('cls')
                list()
                print('Ops!, type only [1] or [2] or [3]')
                sleep(2)
        except:
            print('Ops!, type only [1] or [2] or [3]')
            