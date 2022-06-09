from modulos import escreva, funcao2grau, continuar

escreva('BEM VINDO À CALCULADORA DE FUNÇÕES')

opcao = int(input('''Escolha uma opção: 
(1) -> Função 2° grau
(2) -> Função exponencial
(3) -> Função logarítmica
(4) -> Matriz
(5) -> Sair
Opção: '''))

print()
if opcao == 1:
    escreva('VOCÊ ESCOLHEU FUNÇÃO DE 2° GRAU')

    print('\nf(x) = ax² + bx + c')
    a = float(input('Insira o valor do A: '))
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))

    continuar2grau = 's'                                        #Flag pro while
    while continuar2grau in 's':                                   
        opcao_2grau = int(input('''Escolha uma opção:
    (1) -> Calcular raízes
    (2) -> Calcular função com valor de x
    (3) -> Calcular vértice
    (4) -> Gerar gráfico
    (5) -> Todos
    (6) -> Voltar'''))

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