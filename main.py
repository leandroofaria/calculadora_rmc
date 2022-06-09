from modulos import escreva, funcao2grau, continuar, menu

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
    \033[1;31m(6)\033[m -> Voltar'''))

        if opcao_2grau == 1:
            print(funcao2grau(a,b,c,1))
            continuar2grau = continuar()

        elif opcao_2grau == 2:
            x = int(input('Insira o valor de X: '))
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

        