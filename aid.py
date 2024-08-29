# This file will be used to create functions that will be used in the development of the project.
import aesthetics as ae

#creating initial screen and firts options:
def initial_screen():
    ae.title(ae.colors('TASK LIST', 'amarelo'))
    print(ae.colors('[1]', 'azul claro'), ae.colors(' <Create a new list task>', 'amarelo'))
    print(ae.colors('[2]', 'azul claro'), ae.colors(' <Close the program>', 'amarelo'))
    print('-' * 50)
    answer = validation()


# creating validation of data:
def validation():
    while True:
        try:
            answer_client = int(input('Type [1] to create a new task list or [2] to close the program: '))
            if answer_client == 1 or answer_client == 2:
                return answer_client
            else:
                print('Ops!, type only [1] or [2]')
        except:
            print('Ops!, type only [1] or [2]')