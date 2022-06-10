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

    delta = (b**2) - (4 * a * c)
    if delta < 0:
        delta *= -1
        raiz1 = (f'{(-b/(2*a))} + {sqrt(delta):.2f}i')
        raiz2 = (f'{(-b/(2*a))} - {sqrt(delta):.2f}i')
        return (f'\nAs raízes são: x1 = {raiz1} e x2= {raiz2}')

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

def funcaoexp(a,b,tipo,x=0):
    if tipo == 1:
        if a < 0:
            resposta = 'A função não existe'
        elif a>0 and a<1:
            resposta = 'A função é decrescente'
        elif a>1:
            resposta = 'A função é crescente'
    
    elif tipo == 2:
        funcao_y = a * (b**x)
        resposta = f'O valor da função é {funcao_y}'

    return resposta