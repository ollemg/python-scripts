#!/usr/bin/python3.7
import re
def menu():
    return print("Bem Vindo! \nCalculadora\nMenu:\n[S]omar\ns[U]bitrair\n[M]ultiplicar\n[D]ividir\ns[A]ir")
def entrar():
    num1=int(input("Digite o primeiro valor:"))
    num2=int(input("Digite o segundo valor:"))
    return num1,num2
def somar(entrada1, entrada2):
    return entrada1 + entrada2
def subtrair(entrada1, entrada2):
    return entrada1 - entrada2
def multiplicar(entrada1, entrada2):
    return entrada1 * entrada2
def dividir(entrada1, entrada2):
    return entrada1 / entrada2
menu()
while True:
    opcao=(input("Digite a operacao desejada:"))
    if (opcao == "A" or opcao == "a"):
        break
    else:
        num1, num2 = entrar()
        if (opcao == "u" or opcao == "U"):
            resultado = subtrair(num1,num2)
            print(resultado)
        elif (opcao == "m" or opcao == "M"):
            resultado = multiplicar(num1,num2)
            print(resultado)
        elif (opcao == "d" or opcao == "D"):
            resultado = dividir(num1,num2)
            print(resultado)
        elif (opcao == "S" or opcao == "s"):
            resultado = somar(num1,num2)
            print(resultado)