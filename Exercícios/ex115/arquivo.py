from time import sleep
import os

def verificaArquivo(file):
    try:
        arquivo = open(file, 'r')  # abre arquivo
        arquivo.close()  # fecha
    except FileNotFoundError:  # se falhou false, se deu bom true
        return False
    else:
        return True


def criaArquivo(file):
    try:
        arquivo = open(file, 'wt+')
        arquivo.close()
    except:
        print("Falha na criação do arquivo!")


def limpaArquivo(file):
    arquivo = open(file, 'w+')
    arquivo.close()
    os.remove(file)

def leArquivo(file):
    print("\033[1;31m-\033[m" * 40)
    print("JOGADORES CADASTRADOS".center(40))
    print("\033[1;31m-" * 40)
    print(f"NOME".ljust(31) + "Nº\033[m")
    arquivo = open(file, 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        ind_virgula = linha.find(',')
        nome = linha[:ind_virgula]
        num = linha[ind_virgula+2:len(linha)-1]
        print(f"{nome}".ljust(30), f"{num}")
        sleep(0.5)


def cadastrajog(file):
    jogador = str(input("Nome do jogador: "))
    num = str(input("Numero da camisa: "))
    arquivo = open(file, 'at+')
    arquivo.seek(0)
    linhas = arquivo.readlines()
    flag = True
    for linha in linhas:
        ind_virgula = linha.find(',')
        if jogador == linha[:ind_virgula] or num == linha[ind_virgula+2:len(linha)-1]:
            flag = False
    if not flag:
        print("\033[1;31m-" * 40)
        print("Já possuí um jogador com esse nome ou nº\nde camisa cadastrado!")
    else:
        arquivo.write(f"{jogador}, {num}\n")
        print("\033[1;31m-" * 40)
        print("Jogador cadastrado com sucesso!")


def removejog(file):
    leArquivo(file)
    print("\033[1;31m-" * 40)
    jogador = str(input("\033[1;31m-\033[m Nome do jogador a ser removido:\n\033[1;31m---->\033[m "))
    arquivo = open(file, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open(file, 'w')
    achou = False
    for linha in linhas:
        ind_virgula = linha.find(',')
        if jogador != linha[:ind_virgula]:
            arquivo.write(linha)
        else:
            achou = True
    if achou:
        print(f"Jogador '{jogador}' removido com sucesso!")
    else:
        print(f"Jogador '{jogador}' não encontrado no cadastro!")
