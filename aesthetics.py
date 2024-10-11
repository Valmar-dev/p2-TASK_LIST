# this file will be used to customize the screen.

# creating a fuction that generates titles:
def title(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)


#creating a function to add colors:
def colors(text, color):
    paletas = {
        'preto': f'\033[30m{text}\033[m',
        'vermelho': f'\033[31m{text}\033[m',
        'verde': f'\033[32m{text}\033[m',
        'amarelo': f'\033[33m{text}\033[m',
        'azul escuro': f'\033[34m{text}\033[m',
        'roxo': f'\033[35m{text}\033[m',
        'azul claro': f'\033[36m{text}\033[m',
    }
    return paletas[color]
