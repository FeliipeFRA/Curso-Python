from time import sleep
import arquivo
file = 'C:/Users/SME 01/Desktop/teste.txt'
def menu():
    print("\033[1;31m-"* 40)
    print("CLUBE DE REGATAS DO FLAMENGO".center(40))
    print("\033[m   Relação Jogadores do Clube".center(40))
    while True:
        print("\033[1;31m-\033[m" * 40)
        print("MENU PRINCIPAL".center(40))
        print("\033[1;31m-\033[m" * 40)
        print("\033[1;31m1 -\033[m Cadastrar jogador")
        print("\033[1;31m2 -\033[m Jogadores cadastrados")
        print("\033[1;31m3 -\033[m Remover Jogador")
        print("\033[1;31m4 -\033[m Sair do Sistema")
        print("\033[1;31mX -\033[m Excluir cadastro")
        op = str(input("\033[1;31m---->\033[m "))
        if op == '1':
            print("\033[1;31m-" * 40)
            if not arquivo.verificaArquivo(file):
                try:
                    arquivo.criaArquivo(file)
                except:
                    print("\033[1;31m-" * 40)
                    print("\033[1;31mFinalizando sistema...\033[m")
                    print("\033[1;31m-" * 40)
                    sleep(1)
                    exit(0)
            arquivo.cadastrajog(file)
        elif op == '2':
            arquivo.leArquivo(file)
        elif op == '3':
            arquivo.removejog(file)
        elif op == '4':
            print("\033[1;31m-" * 40)
            print("\033[1;31mFinalizando sistema...\033[m")
            print("\033[1;31m-" * 40)
            sleep(1)
            exit(0)
        elif op == 'X':
            print("\033[1;31m-" * 40)
            print("\033[mTodos os dados serão \033[1;31mEXCLUÍDOS PERMANENTEMENTE\033[m, tem certeza?")
            confirm = str(input("\033[1;31m[Digite 'SIM' para confirmar] ---> "))
            print("\033[1;31m-" * 40)
            if confirm == 'SIM':
                print("Arquivo limpo com sucesso!")
                arquivo.limpaArquivo(file)
            else:
                print("Falha na confirmação! Operação cancelada...")
            sleep(1)
        else:
            print("\033[1;31m-" * 40)
            print("OPÇÃO INVÁLIDA! Tente novamente\033[m")
            sleep(1)
