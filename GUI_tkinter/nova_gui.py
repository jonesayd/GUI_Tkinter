from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog #Fornece classes e funções de fábrica para criar janelas de seleção de arquivo/diretório
import cv2 #Biblioteca OpenCV para o desenvolvimento de aplicativos na área de visão computacional
import imutils #Pacote baseado em OPenCV para implementar uma série de operações em imagens (translação, rotação, dimensionamento e esqueletização)
import os #Serve para navegar dentro das pastas do PC
import pandas as pd

janela_princ = Tk()
icon = PhotoImage(file="icon_ton.png") #Para trocar o ícone da janela principal. Obs.: No endereço da imagem sempre colocar mais uma barra nas já existentes para não dar erro
janela_princ.iconphoto(True, icon)



# Classe criada para identificar com funções dentro dessa classe o que cada coisa faz
class Application():  

    # O "init" serve para inicializar a classe. Aqui estarão as características do que será feito
    def __init__(self):  
                
        self.janela_princ = janela_princ # Como a variável 'janela_princ = Tk()' (linha 8) não está dentro da Classe, deve-se criar uma equivalência para que possa rodar
        self.tela()  # Chamando a função tela
        self.janela_topo()
        self.frame_da_tela()
        self.logo_no_frame()
        self.nome_programa()
        self.instrucoes()
        self.selecao_imagem_frame()
        self.selecao_imagem1_frame()
        self.botao_abrir()
        self.janela_da_imagem()
        self.caminho_imagem()   
        janela_princ.mainloop()

            
    #É a 'main window'
    def tela(self):
        self.janela_princ.title("Detector de Cores")  # Título da Janela
        self.janela_princ.configure(background="#DCDCDC")  # Cor de fundo
        self.janela_princ.geometry("1000x600") # Tamanho que será inicializada a tela
        self.janela_princ.resizable(False, False) #Para a tela ficar fixa, não mudar do tamanho da linha acima

    #Definindo a função para criar uma janela no topo na cor grafite para enfeitar a GUI
    def janela_topo(self): 
        self.janela_1= Label(self.janela_princ, bg="#363636")
        self.janela_1.place(relx=0, rely=0, relwidth=10, relheight=0.4, )

    #Definindo a função para criar o frame central onde está a 'logo', instruções e o frame/janela onde será mostrada a imagem
    def frame_da_tela(self):
        self.frame_central= Frame(self.janela_princ, bg="#fff")
        self.frame_central.place(relx=0.05, rely=0.11, relwidth=0.9, relheight=0.8)
    
    #Definindo a função para colocar a logo do programa
    def logo_no_frame(self): 
        self.img_logo= PhotoImage(file="logo_ton.png")
        self.logo= Label(self.frame_central, image=self.img_logo, bg="#fff")
        self.logo.place(x=10, y=10)
    
    #Definindo a função para criação da janela com o nome do programa
    def nome_programa(self): 
        self.nome_prog= Label(self.janela_1, text="TON - Detector de Cores", font="arial 25 bold", foreground="white", bg="#363636")
        self.nome_prog.place(x=45, y=10)

    #Definindo a função para criar a janela de instruções para uso do programa
    def instrucoes(self): 
        self.instruc= Label(self.frame_central, text="INSTRUÇÕES:", font="arial 10 bold", bg="white")
        self.instruc.place(x=20, y=170)
        
        self.instruc1= Label(self.frame_central, text="1. Escolha sua imagem", font="arial 10", bg="white")
        self.instruc1.place(x=20, y=200)

        self.instruc2= Label(self.frame_central, text="2. Dê 2 cliques na cor desejada", font="arial 10", bg="white")
        self.instruc2.place(x=20, y=220)

        self.instruc3= Label(self.frame_central, text="3. Será mostrado:", font="arial 10", bg="white")
        self.instruc3.place(x=20, y=240)

        self.instruc4= Label(self.frame_central, text="    - Nome da cor", font="arial 10", bg="white")
        self.instruc4.place(x=20, y=260)

        self.instruc5= Label(self.frame_central, text="    - Valor em hexadecimal", font="arial 10", bg="white")
        self.instruc5.place(x=20, y=280)

        self.instruc6= Label(self.frame_central, text="    - Valor em RGB", font="arial 10", bg="white")
        self.instruc6.place(x=20, y=300)
    
    #Definindo a função para criar o frame de trás (moldura cinza) onde irá aparecer a imagem
    def selecao_imagem_frame(self): 
        self.sel_img= Frame(self.janela_princ, width=620, height=430, bg="#d6dee5") #Tamanho do frame, sendo CxA e cor do frame
        self.sel_img.place (x=300, y=90) #Posição do frame dentro da janela, sendo 'x' horizontal e 'y' vertical
    
    #Definindo a função para criar o frame da frente (preto) onde irá aparecer a imagem
    def selecao_imagem1_frame(self): 
        self.sel_img1= Frame(self.sel_img, bd=3, bg="black", width=600, height= 410, relief=GROOVE) #O 'relief=GROOVE' serve para criar a moldura entre o frame cinza e o preto. Os demais são: FLAT, RAISED, SUNKEN e RIDGE.
        self.sel_img1.place(x=10, y=10)
    
    #Definindo a função para criar o Botão "Abrir Imagem" 
    def botao_abrir(self):
        self.botaoabrir= Button(self.frame_central, text="Abrir Imagem", width=12, height=1, font="arial 11 bold", command=self.caminho_imagem)
        self.botaoabrir.place(x=50, y=360)

    #Definindo a função para criar a janela onde aparecerá a imagem dentro do frame 'self.sel_img1'
    def janela_da_imagem(self):
        self.janela_imagem= Label (self.sel_img1, bg="black")
        self.janela_imagem.place(x=0, y=0)
    
    #Definição da função de escolha e abertura da imagem na janela acima
    def caminho_imagem(self):
        self.caminho_img = filedialog.askopenfilename(title="Abrir Imagem", filetypes= [ #Especificar os tipos de arquivos
            ("Arquivo JPG", ".jpg"),
            ("Arquivo JPEG", ".jpeg"),
            ("Arquivo PNG", ".png"),])
        
        if len (self.caminho_img) > 0:
            global imagem

            #Ler a imagem de entrada
            imagem = cv2.imread(self.caminho_img)
            imagem = imutils.resize(imagem, width=590, height=400) #Para ajustar a imagem e não ultrapassar o tamanho da janela

            #Para visualizar a imagem de entrada na GUI
            imagem_para_mostrar = imutils.resize (imagem, width=590, height=400) #Tamanho que a imagem escolhida é mostrada na tela
            imagem_para_mostrar = cv2.cvtColor (imagem_para_mostrar, cv2.COLOR_BGR2RGB)
            im = Image.fromarray (imagem_para_mostrar) #As linhas 117, 118, 120 e 121 são responsáveis por fazer aparecer a imagem da variável 'imagem_para_mostrar' na GUI
            img = ImageTk.PhotoImage (image=im)
           
            self.janela_imagem.configure (image=img)
            self.janela_imagem.image = img



Application()
