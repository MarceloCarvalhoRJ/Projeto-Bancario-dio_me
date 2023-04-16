from termcolor import colored, cprint
from emoji import emojize, demojize


def letreiro(texto, cor1, cor2):
    print(colored(' ' + '=' * 35 + ' ', cor2))
    print(colored(f"{emojize(':star:')}{colored(texto.center(33), cor1)}{emojize(':star:')}"))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored(' ' + '=' * 35 + ' ', cor2))

def letreiro_2(texto, cor1, cor2):
    print(colored('-' * len(texto), cor2))
    print(colored((texto + emojize(' :grinning_face_with_big_eyes:')).center(35), cor1))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored('-' * len(texto), cor2))

def letreiro_fundo(texto, cor_fundo):
    """
    funcao traz um letreiro com um titulo
    -> a linha superior e inferior acompanham o tamanho do texto
    -> recebe 2 argumentos, sendo o texto e a cor de fundo (usar on_'nome da cor' ex: on_green).
    -> retorna o letreiro personalizado
    """

def cor(c):
    cor = (
    '\033[m',         # 0 - sem cores 
    '\033[0;30;41m',  # 1 - Branco em Vermelho
    '\033[0;30;42m',  # 2 - Branco em Verde
    '\033[0;30;43m',  # 3 - Branco em Amarelo
    '\033[0;30;44m',  # 4 - Branco em Azul
    '\033[0;30;45m',  # 5 - Branco em Roxo
    '\033[0;30;46m',  # 6 - Branco em Ciano
    '\033[7;30m',     # 7 - Branco 
    )
    return cor[c]


if __name__ == '__main__': #serve para nao carregar o que estiver abaixo do if quando chamar a funcao.
    print(f'Hello, {cor(2)}World')
   


