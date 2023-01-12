import customtkinter
from tkinter import *
import array

customtkinter.set_appearance_mode("light")
window = customtkinter.CTk()
window.geometry("500x600")
window.title("App")
window.minsize(500,600)

campo = customtkinter.CTkFrame(window,width=500, height=600)
campo.place(relx=0.5, rely=0.5, anchor=CENTER)

#text box
textbox1 = customtkinter.CTkEntry(campo, width=160, height=40, placeholder_text="X: -3.00")
textbox1.place(x=270, y=510)

textbox2 = customtkinter.CTkEntry(campo, width=160, height=40, placeholder_text="Y: 1.20")
textbox2.place(x=270, y=550)

textbox3 = customtkinter.CTkEntry(campo, width=200, height=40, placeholder_text="Função primeiro grau")
textbox3.place(x=40, y=510)

#espaço do plano cartesiano
frame1 = customtkinter.CTkFrame(master=campo, width=500, height=500)
frame1.place(x=0, y=0)

#gerarnumeros

distanciaNumeros = 25
i = 0
n = 10

for c in range(0, 10):
    i += 1
    n += 1

    #numero horizontal
    label1 = customtkinter.CTkLabel(campo, text=i-11)
    label1.place(x=(i*distanciaNumeros)-25, y=250)

    label2 = customtkinter.CTkLabel(campo, text=n-11)
    label2.place(x=(n*distanciaNumeros)-25, y=250)

    #numero vertical
    label3 = customtkinter.CTkLabel(campo, text=(i-11) * -1)
    label3.place(x=250,y=(i*distanciaNumeros)-25)

    label4 = customtkinter.CTkLabel(campo, text=(n-11) * -1)
    label4.place(x=250,y=(n*distanciaNumeros)-25)

    #quadriculado horizontal
    pontoVertical1 = Frame(frame1, width=1, height=500, background="red")
    pontoVertical1.place(x=(n*distanciaNumeros)-25,y=0)

    pontoVertical2 = Frame(frame1, width=1, height=500, background="red")
    pontoVertical2.place(x=i*distanciaNumeros,y=0)

    #quadriculado vertical
    pontoHorizontal1 = Frame(frame1, width=500, height=1, background="red")
    pontoHorizontal1.place(x=0,y=(i*distanciaNumeros)-25)

    pontoHorizontal2 = Frame(frame1, width=500, height=1, background="red")
    pontoHorizontal2.place(x=0,y=(n*distanciaNumeros)-25)

def carregar():
    if textbox1.get() != "" and textbox2.get() != "":
        posiX = (float(textbox1.get()) * distanciaNumeros) + 250 -4
        posiY = -(float(textbox2.get()) * distanciaNumeros) + 250 -4

        #label = customtkinter.CTkLabel(window, text=i)
        #label.place(x=posiX+8, y=posiY+8)

        marcaCartesiano1 = Frame(frame1, width=8, height=8, background="blue")
        marcaCartesiano1.place(x=posiX,y=posiY)

#Gerar Função
ix = -250
iy = 0
def funcaoGrau():
    if textbox3.get() != "":
        global ix
        global iy
        formula = textbox3.get()
        formula.split()

        ax = float(formula[1])
        ay = float(formula[3])

        for c in range(0, 500):
            ix += 1
            calculo = ix * ax + ay
            if ay > 0:
                calculo = -calculo

            zy = 0
            zy = -ay/ax
            # 0 = x4 -8

            if calculo < 250 and calculo > -250:
                FormatoFuncao = Frame(frame1, width=4, height=4, background="blue")
                FormatoFuncao.place(x=(ix + 250) -(zy * distanciaNumeros),y=calculo+250)

            if ix > 500:
                ix = 0
                iy = 0

#Tema Escuro
oi = True
def temaEscuro():
    global oi

    if oi:
        customtkinter.set_appearance_mode("dark")
        oi = False
    else:
        customtkinter.set_appearance_mode("light")
        oi = True

Dvr = customtkinter.CTkLabel(campo, text="D:0.01")
Dvr.place(x=4,y=580)

#Botões
button1 = customtkinter.CTkButton(campo, width=50, height=80, text="Adc\nPonto", command=carregar)
button1.place(x=430,y=510)

button2 = customtkinter.CTkButton(campo, width=180, height=30, text="resolver função", command=funcaoGrau)
button2.place(x=50,y=560)

button3 = customtkinter.CTkButton(campo, width=40, height=30, text="Tema", command=temaEscuro)
button3.place(x=0,y=0)

window.mainloop()