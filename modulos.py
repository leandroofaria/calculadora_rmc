from math import sqrt

def menu():
    escolha = int(input('''Escolha uma opção: 
\033[1;36m(1) -> Função 2° grau\033[m
\033[1;35m(2) -> Função exponencial\033[m
\033[1;34m(3) -> Função logarítmica\033[m
\033[1;32m(4) -> Matriz\033[m
\033[1;31m(5) -> Sair\033[m
Opção: '''))
    return escolha

def escreva(texto):
    print('-' * (len(texto)))
    print(f'     {texto}')
    print('-' * (len(texto)))

def funcao2grau(a,b,c,tipo,x=0):

    delta = (b**2) - (4 * a * c)            #Encontra as raízes
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)

    funcao_y = (a * (x**2) + (b * x) + c)   #Calcula o valor da função

    xv = -b / (2 * a)
    yv = (delta * -1) / (4 * a)

    if tipo == 1:
        return (f'\nAs raízes são: x1 = {raiz1} e x2= {raiz2}') 
    elif tipo == 2:
        return (f'\nO valor da função é: {funcao_y}')
    elif tipo == 3:
        return (f'\nOs vértices são: Xv={xv} e Yv={yv}')

def continuar():
    resposta = str(input('Deseja ver o resultado de outra opção? (S/N)')).strip().lower()[0]
    if resposta in 'n':
        print('Encerrando programa, volte sempre!')
        resposta = 'n'
    return resposta