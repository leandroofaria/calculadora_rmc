from math import sqrt
from tkinter import YView

def escreva(texto):
    print('-' * (len(texto)+4))
    print(f'  {texto}')
    print('-' * (len(texto)+4))

def funcao2grau(a,b,c,tipo,x=0):

    delta = (b**2) - (4 * a * c)            #Encontra as raízes
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)

    funcao_y = (a * (x**2) + (b * x) + c)   #Calcula o valor da função

    xv = -b / (2 * a)
    yv = (delta * -1) / (4 * a)

    if tipo == 1:
        return (f'As raízes são: x1 = {raiz1} e x2= {raiz2}') 
    elif tipo == 2:
        return (f'O valor da função é: {funcao_y}')
    elif tipo == 3:
        return (f'Os vértices são: Xv={xv} e Yv={yv}')

def continuar():
    resposta = str(input('Deseja ver o resultado de outra opção? (S/N)')).strip().lower()[0]
    if resposta in 'n':
        print('Encerrando programa, volte sempre!')
        resposta = 'n'
    return resposta