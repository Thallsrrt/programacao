#!/usr/bin/python

import os, sys

os.system("clear")

def login():
    var=1
    while var == 1 : 
        os.system("clear")
        user = raw_input("Digite o Usuario: ")
        passw = raw_input("Digite a Senha: ")
        usu="lucas"
        senha="senai"
        if user == usu :
            if passw == senha :
                os.system("clear")
                print("Login Correto")
                os.system("sleep 2")
                os.system("clear")
                menu()
                
            else :
                os.system("clear")
                print("Senha Incorreta")
                os.system("sleep 2")
                os.system("clear")

        else :
            os.system("clear")
            print("Login Incorreto")
            os.system("sleep 2")
            os.system("clear")

def SOMA():
    os.system("clear")
    print("Voce Escolheu Soma!!")
    num1 = input("Digite o Primeiro numero a ser somado: ")
    num2 = input("Digite o Segundo numero a ser somado: ")
    soma = num1 + num2
    print('A soma dos numeros e: ', soma)
    os.system("sleep 2")
    os.system("clear")
    menu()

def SUBT():
    os.system("clear")
    print("Voce Escolheu Subtracao!!")
    num1 = input("Digite o Primeiro numero a ser subtraido: ")
    num2 = input("Digite o Segundo numero a ser subtraido: ")
    sub = num1 - num2
    print('A subtracao dos numeros e: ', sub)
    os.system("sleep 2")
    os.system("clear")
    menu()

def MULT():
    os.system("clear")
    print("Voce Escolheu Multiplicacao!!")
    num1 = input("Digite o Primeiro numero a ser multiplicado: ")
    num2 = input("Digite o Segundo numero a ser multiplicado: ")
    mult = num1 * num2
    print('A multiplicacao dos numeros e: ', mult)
    os.system("sleep 2")
    os.system("clear")
    menu()

def DIV():
    os.system("clear")
    print("Voce Escolheu Divisao!!")
    num1 = input("Digite o Primeiro numero a ser dividido: ")
    num2 = input("Digite o Segundo numero a ser dividido: ")
    div = num1 / num2
    print('A divisao dos numeros e: ', div)
    os.system("sleep 2")
    os.system("clear")
    menu()

def BASC():
    os.system("clear")
    print("Voce Escolheu Basckara!!")
    a = input("Digite A: ")
    b = input("Digite B: ")
    c = input("Digite C: ")
    delta = b ** 2 - 4 * a * c
    if delta < 0 :
        print('Delta Negativo, Nao ha raiz real')
        os.system("sleep 2")
        os.system("clear")
        menu()

    print('Delta e igual a: ', delta)
    os.system("sleep 2")
    x1 = -b + (delta ** 0.5)
    x12 = x1 / 2 * a
    x2 = -b - (delta ** 0.5)
    x22 = x2 / 2 * a
    print('Os valores sao: ', x12, x22)
    os.system("sleep 2")
    os.system("sleep 2")
    os.system("clear")
    menu()

def menu():
    var=1
    while var == 1 :
        print("Ola, Bem-Vindo a calculadora do Linux")
        print("Qual opcao voce deseja?")
        print("0 --> Soma")
        print("1 --> Subtracao")
        print("2 --> Multiplicacao")
        print("3 --> Divisao")
        print("4 --> Baskhara")
        print("5 --> Sair")
        print("")
        OPCAO = raw_input("Qual Numero voce deseja?: ")
    
        while OPCAO != 6 :
            if OPCAO == "0" :
                SOMA()
            if OPCAO == "1" :
                SUBT()
            if OPCAO == "2" :
                MULT()
            if OPCAO == "3" :
                DIV()
            if OPCAO == "4" :
                BASC()
            if OPCAO == "5" :
                os.system("clear")
                print("Bye Bye!!")
                os.system("sleep 2")
                os.system("clear")
                OPCAO=6
                sys.exit()
            if OPCAO != "0,1,2,3,4,5" :
                os.system("clear")
                print("Opcao Invalida")
                os.system("sleep 2")
                os.system("clear")
                OPCAO=6

login()
