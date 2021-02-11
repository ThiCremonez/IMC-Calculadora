# --------------------------------------------------------------------- #
# Name: "Calculadora de IMC"
# Version: "1.0.0"
# Description: "Realiza o Cálculo de Índice de Massa Corporal (IMC)"
# Author: ThiCremonez
# Language: pt-br
# --------------------------------------------------------------------- #

from tkinter import *

janela = Tk()


def indice_de_massa_corporal(peso, altura):  # função que calcula o IMC
    imc = peso / altura ** 2
    return imc


def bt_click():
    num1 = str(ed1.get())
    num2 = str(ed2.get())
    num3 = float(num1.replace(',', '.'))  # converte a string peso em float e substitui a vírgula
    num4 = float(num2.replace(',', '.'))  # converte a altura e converte em float e substitui a vírgula

    if indice_de_massa_corporal(num3, num4) < 18.5:
        lb5["text"] = "Seu IMC é %1.2f \n Magreza \n Grau de obesidade = 0" % (indice_de_massa_corporal(num3, num4))
    elif 18.5 <= indice_de_massa_corporal(num3, num4) < 25:
        lb5["text"] = "Seu IMC é %1.2f \n Normal \n Grau de obesidade = 0" % (indice_de_massa_corporal(num3, num4))
    elif 25 <= indice_de_massa_corporal(num3, num4) < 30:
        lb5["text"] = "Seu IMC é %1.2f \n Sobrepeso \n Grau de obesidade = I" % (indice_de_massa_corporal(num3, num4))
    elif 30 <= indice_de_massa_corporal(num3, num4) < 40:
        lb5["text"] = "Seu IMC é %1.2f \n Obesidade \n Grau de obesidade = II" % (indice_de_massa_corporal(num3, num4))
    else:
        lb5["text"] = "Seu IMC é %1.2f \n Obesidade Grave \n Grau de obesidade = III" % (
            indice_de_massa_corporal(num3, num4))


lb1 = Label(janela, text="----Cálculo de IMC----", bg="light grey")
lb2 = Label(janela, text="Digite seu peso em 'kg':")
lb3 = Label(janela, text="Digite sua altura em 'metros':")
lb4 = Label(janela, text="Resultado: ")
lb5 = Label(janela, text="")  # mostra o resultado

ed1 = Entry(janela)
ed2 = Entry(janela)

bt = Button(janela, text="Calcular", command=bt_click)

lb1.grid(row=10, column=10, columnspan=20, sticky=W + E)

lb2.grid(row=20, column=10, sticky=E)
lb3.grid(row=30, column=10, sticky=E, pady=(0, 20))
lb4.grid(row=50, column=10, ipady=20, pady=(0, 40))
lb5.grid(row=50, column=20, pady=(0, 40))

ed1.grid(row=20, column=20, sticky=W)
ed2.grid(row=30, column=20, sticky=W, pady=(0, 20))

bt.grid(row=40, column=20, columnspan=10, sticky=W + E)

janela.title("Cálculo de IMC")
janela.geometry("300x200+200+200")
janela.mainloop()
