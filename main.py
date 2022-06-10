from modulos import criar_matriz, escreva, funcao2grau, continuar, funcaoexp, menu, criar_matriz

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
            print(funcao2grau(a,b,c,1))
            continuar2grau = continuar()

        elif opcao_2grau == 2:
            x = float(input('Insira o valor de X: '))
            print(funcao2grau(a,b,c,2,x))
            continuar2grau = continuar()

        elif opcao_2grau == 3:
            print(funcao2grau(a,b,c,3))
            continuar2grau = continuar()
        
        elif opcao_2grau == 4:
            pass

        elif opcao_2grau == 5:
            x = int(input('Insira o valor de X: '))
            print(funcao2grau(a,b,c,1))
            print(funcao2grau(a,b,c,2,x))
            print(funcao2grau(a,b,c,3))
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
    escreva('\033[1;34mVOCÊ ESCOLHEU MATRIZ\033[m')

    numLinhas = int(input('Número de linhas da matriz: '))
    numColunas = int(input('Número de colunas da matriz: '))

    matrizfeita = criar_matriz(numLinhas, numColunas)

    continuarmat = 's'
    while continuarmat in 's':
        opcaomat = int(input('''\nEscolha uma opção:
        \033[1;36m(1)\033[m -> Determinante
        \033[1;35m(2)\033[m -> Multiplicação de matrizes
        \033[1;34m(3)\033[m -> Matriz transposta
        \033[1;33m(4)\033[m -> Todos
        \033[1;31m(5)\033[m -> Voltar
        Opção: '''))

        if opcaomat == 1:
            if numLinhas == numColunas:
                print('É uma matriz quadrada')
                if numLinhas == 3 and numColunas == 3:

                    soma_dprincipal = matrizfeita[0][0] * matrizfeita[1][1] * matrizfeita[2][2] + \
                    matrizfeita[0][1] * matrizfeita[1][2] * matrizfeita[2][0] + \
                    matrizfeita[0][2] * matrizfeita[1][0] * matrizfeita[2][1]

                    SomaDiagSecun = matrizfeita[2][0] * matrizfeita[1][1] * matrizfeita[0][2] + \
                    matrizfeita[2][1] * matrizfeita[1][2] * matrizfeita[0][0] + \
                    matrizfeita[2][2] * matrizfeita[1][0] * matrizfeita[0][1] 
                    continuarmat = continuar()






