import getpass
import os

class Forca():

    def __init__(self,palavra):
        self.palavra=[]
        self.palavra_vazia=[]
        self.jogo_rodando = True
        self.contador_erros = 0
        for letra in palavra:
            self.palavra.append(letra)
        for i in range(0,len(palavra)):
            self.palavra_vazia.append("_")

    def verificarLetra(self,letra):
        contador = self.palavra.count(letra)
        if (contador>0):
            for index,let in enumerate(self.palavra):
                if (letra == let):
                    self.palavra_vazia[index] = let
            return True
        else:
            self.contador_erros+=1
            print("Você errou!")
            return False

    def imprimirPalavra(self):
        for letra in self.palavra_vazia:
            print (letra + " ", end="", flush=True)

    def imprimirEstadoAtual(self):
        if(self.contador_erros == 0):
            print(" _____")
            print("|     |")
            print("      |")
            print("      |")
            print("      |")
            self.imprimirPalavra()
        elif(self.contador_erros == 1):
            print(" _____")
            print("|     |")
            print("o     |")
            print("      |")
            print("      |")
            self.imprimirPalavra()
        elif(self.contador_erros == 2):
            print(" _____")
            print("|     |")
            print("o     |")
            print("|     |")
            print("      |")
            self.imprimirPalavra()
        elif(self.contador_erros == 3):
            print(" _____")
            print("|     |")
            print("o     |")
            print("|     |")
            print("/     |")
            self.imprimirPalavra()
        elif(self.contador_erros == 4):
            print(" _____")
            print("|     |")
            print("o     |")
            print("|     |")
            print("/\    |")
            self.imprimirPalavra()
        elif(self.contador_erros == 5):
            print("  _____")
            print(" |     |")
            print(" o     |")
            print("/|     |")
            print(" /\    |")
            self.imprimirPalavra()
        elif(self.contador_erros == 6):
            print("  _____")
            print(" |     |")
            print(" o     |")
            print("/|\    |")
            print(" /\    |")
            self.imprimirPalavra()
        elif(self.contador_erros == 7):
            print("  _____")
            print(" |     |")
            print(" X     |")
            print("/|\    |")
            print(" /\    |")
            self.imprimirPalavra()
            print("\nVocê perdeu o jogo!")
            self.jogo_rodando = False




    def ganhouJogo(self):
        if (self.palavra == self.palavra_vazia):
            self.jogo_rodando = False
            return True
        else:
            return False

palavra_escolhida = getpass.getpass("Informe uma palavra para o jogo da Forca>>>",stream=None)
jogo_forca = Forca(palavra_escolhida)
while(jogo_forca.jogo_rodando):
    if (jogo_forca.palavra_vazia.count('_')==len(jogo_forca.palavra_vazia) and jogo_forca.contador_erros == 0):
        print(" _____")
        print("|     |")
        print("      |")
        print("      |")
        print("      |")
        jogo_forca.imprimirPalavra()
    letra_escolhida = input("\n\nInforme uma letra:")
    jogo_forca.verificarLetra(letra_escolhida)
    os.system("cls")
    jogo_forca.imprimirEstadoAtual()
    if(jogo_forca.ganhouJogo()):
        print("\nVocê ganhou, parabéns!")



    



