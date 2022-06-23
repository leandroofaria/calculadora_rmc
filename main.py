from math import sqrt

import numpy as np

def menu():
    escolha = int(input('''Escolha uma opção: 
\033[1;36m(1) -> Função 2° grau\033[m
\033[1;35m(2) -> Função exponencial\033[m
\033[1;32m(3) -> Matriz\033[m
\033[1;31m(4) -> Sair\033[m
Opção: '''))
    return escolha

def escreva(texto):
    print('-' * (len(texto)))
    print(f'     {texto}')
    print('-' * (len(texto)))

def raizes2grau(a,b,c):

    delta = (b**2) - (4 * a * c)
    if delta < 0:
        delta *= -1
        raiz1 = (f'{(-b/(2*a))} + {sqrt(delta):.2f}i')
        raiz2 = (f'{(-b/(2*a))} - {sqrt(delta):.2f}i')
        return (f'\nAs raízes são: x1 = {raiz1} e x2= {raiz2}')

    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)


    return (f'\nAs raízes são: x1 = {raiz1} e x2= {raiz2}') 


def valorfuncao2grau(a,b,c,x):
    funcao_y = (a * (x**2) + (b * x) + c)   #Calcula o valor da função
    return (f'\nO valor da função é: {funcao_y}')

def vertices2grau(a,b,c):
    delta = (b**2) - (4 * a * c)
    xv = -b / (2 * a)
    yv = (delta * -1) / (4 * a)
    return (f'\nOs vértices são: Xv={xv} e Yv={yv}')



def continuar():
    resposta = str(input('Deseja ver o resultado de outra opção? (S/N)')).strip().lower()[0]
    if resposta in 'n':
        print('Encerrando programa, volte sempre!')
        resposta = 'n'
    return resposta

def funcaoexp(a,b,tipo,x=0):
    if tipo == 1:
        if b < 0:
            resposta = 'A função não existe'
        elif b>0 and a<1:
            resposta = 'A função é decrescente'
        elif b>1:
            resposta = 'A função é crescente'
    
    elif tipo == 2:
        funcao_y = a * (b**x)
        resposta = f'O valor da função é {funcao_y}'

    return resposta

def criar_matriz(linhas, colunas):
    matriz = [0] * linhas
    for linha in range(linhas):
        matriz[linha] = [0] * colunas

    for linha in range(linhas):
        for coluna in range(colunas):
            matriz[linha][coluna] = int(input(f'Insira o número para a posição [{linha}][{coluna}] da matriz: '))

    for linha in range(linhas):
        for coluna in range(colunas):
            print(f'[{matriz[linha][coluna]}]', end= '')
        print()
    return matriz

def multiplicar_matriz(matriz1, matriz2):
    resultado = np.dot(matriz1, matriz2)
    return resultado

def matriz_transposta(matriz):
    transposta = np.transpose(matriz)
    return transposta

escreva('\033[1;33mBEM VINDO À CALCULADORA DE FUNÇÕES\033[m')

opcao = menu()

print()
if opcao == 1:
    escreva('\033[1;36mVOCÊ ESCOLHEU FUNÇÃO DE 2° GRAU\033[m')

    print('\nf(x) = ax² + bx + c')
    a = float(input('Insira o valor do A: '))
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))

    continuar2grau = 's'                                        #Flag pro while
    while continuar2grau in 's':                                   
        opcao_2grau = int(input('''\nEscolha uma opção:
    \033[1;36m(1)\033[m -> Calcular raízes
    \033[1;35m(2)\033[m -> Calcular função com valor de x
    \033[1;34m(3)\033[m -> Calcular vértice
    \033[1;33m(4)\033[m -> Gerar gráfico
    \033[1;32m(5)\033[m -> Todos
    \033[1;31m(6)\033[m -> Voltar
    Opcão: '''))

        if opcao_2grau == 1:
            print(raizes2grau(a,b,c))
            continuar2grau = continuar()

        elif opcao_2grau == 2:
            x = float(input('Insira o valor de X: '))
            print(valorfuncao2grau(a,b,c,x))
            continuar2grau = continuar()

        elif opcao_2grau == 3:
            print(vertices2grau(a,b,c))
            continuar2grau = continuar()
        
        elif opcao_2grau == 4:
            pass

        elif opcao_2grau == 5:
            x = int(input('Insira o valor de X: '))
            print(raizes2grau(a,b,c))
            print(valorfuncao2grau(a,b,c,x))
            print(vertices2grau(a,b,c))

            continuar2grau = continuar()

        elif opcao_2grau == 6:
            menu()

elif opcao == 2:
    escreva('\033[1;35mVOCÊ ESCOLHEU FUNÇÃO EXPONENCIAL\033[m')

    print('\nf(x)= a . b^x')
    a = float(input('Insira o valor de A: '))
    b = float(input('Insira o valor de B: '))

    continuarexp = 's'
    while continuarexp in 's':
        opcaoexp = int(input('''\nEscolha uma opção:
    \033[1;36m(1)\033[m -> Crescente ou Decrescente?
    \033[1;35m(2)\033[m -> Calcular função com valor de x
    \033[1;34m(3)\033[m -> Gráfico
    \033[1;33m(4)\033[m -> Todos
    \033[1;31m(5)\033[m -> Voltar
    Opção: '''))

        if opcaoexp == 1:
            print(funcaoexp(a,b,1))
            continuarexp = continuar()
        elif opcaoexp == 2:
            x = float(input('Insira o valor de X: '))
            print(funcaoexp(a,b,2,x))
            continuarexp = continuar()
        elif opcao == 3:
            pass
        elif opcaoexp == 4:
            x = float(input('Insira o valor de X: '))
            print(funcaoexp(a,b,1))
            print(funcaoexp(a,b,2,x))
            continuarexp = continuar()
        elif opcaoexp == 5:
            menu()

elif opcao == 3:
    escreva('\033[1;32mVOCÊ ESCOLHEU MATRIZ\033[m')

    numLinhas = int(input('Número de linhas da matriz: '))
    numColunas = int(input('Número de colunas da matriz: '))

    matrizfeita = criar_matriz(numLinhas, numColunas)

    continuarmat = 's'
    while continuarmat in 's':
        opcaomat = int(input('''\nEscolha uma opção:
        \033[1;36m(1)\033[m -> Determinante
        \033[1;35m(2)\033[m -> Multiplicação de matrizes
        \033[1;34m(3)\033[m -> Matriz transposta
        \033[1;31m(4)\033[m -> Voltar
        Opção: '''))

        if opcaomat == 1:
            if numLinhas == numColunas:
                print('É uma matriz quadrada')
                if numLinhas == 3 and numColunas == 3:
                    soma_dprincipal = matrizfeita[0][0] * matrizfeita[1][1] * matrizfeita[2][2] + \
                    matrizfeita[0][1] * matrizfeita[1][2] * matrizfeita[2][0] + \
                    matrizfeita[0][2] * matrizfeita[1][0] * matrizfeita[2][1]
                    soma_dsecundaria = matrizfeita[2][0] * matrizfeita[1][1] * matrizfeita[0][2] + \
                    matrizfeita[2][1] * matrizfeita[1][2] * matrizfeita[0][0] + \
                    matrizfeita[2][2] * matrizfeita[1][0] * matrizfeita[0][1] 
                    determinante = soma_dprincipal - soma_dsecundaria 
                    print(f'A determinante da matriz vale {determinante}!')
                    continuarmat = continuar()

                elif numLinhas == 2 and numColunas == 2:
                    soma_dprincipal = matrizfeita[0][0] * matrizfeita[1][1]
                    soma_dsecundaria = matrizfeita[0][1] * matrizfeita[1][0]
                    determinante = soma_dprincipal - soma_dsecundaria
                    print(f'A determinante da matriz vale {determinante}!')
                    continuarmat = continuar()

        if opcaomat == 2:
            numLinhas2 = int(input('Número de linhas da segunda matriz: '))
            numColunas2 = int(input('Número de colunas da segunda matriz: '))

            if numColunas == numLinhas2:
                matrizfeita2 = criar_matriz(numLinhas2, numColunas2)
                print(f'O resultado da multiplicação das matrizes é: ')
                print(multiplicar_matriz(matrizfeita, matrizfeita2))
                continuarmat = continuar()
            else:
                print('Não é possível multiplicar!')
                continuarmat = continuar()

        if opcaomat == 3:
            print(f'A matriz transposta é: ')
            print(matriz_transposta(matrizfeita))
            continuarmat = continuar()








