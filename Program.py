#Imports e bibliotecas 
from cryptography.fernet import Fernet #  /// módulo e biblioteca de criptografia que utilizei para refinamento de projeto \\\
import tkinter as tk #  /// biblioteca do pop-up de contagem de caracteres, não utilizei mas é um projeto que darei continuidade para refinamento e estudo próprio \\\
import os   # /// biblioteca para o salvamento do arquivo. módulo de interação com o S.O. \\\
import subprocess # /// biblioteca para processo do módulo \\\


#tentei usar uma função que aprendi no youtube onde abre uma janela pop-up e nela o usuario coloca a frase e ao mesmo tempo vai aparecendo a quantidade de caracteres

''' 
janela = tk.Tk()
janela.title("Contador de Caracteres")

entry = tk.Entry(janela)
entry.pack(padx=10, pady=10)

caracteres = tk.Label(janela, text="Caracteres: 0")
caracteres.pack(pady=5)

entry.bind("<KeyRelease>", lambda event: contar_caracteres())

janela.mainloop()
''' 

# /// AQUI FORAM CRIADAS FUNÇÕES JUNTAMENTE COM O MÉTODO CRYPTOGRAPHY. \\\

def instalar_modulo(modulo): # /// Função para instalação automática do módulo necessário \\\
    try:
        # Executa o comando pip para instalar o módulo
        subprocess.check_call(["pip", "install", modulo])
        print(f"O módulo {modulo} foi instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o módulo {modulo}. Código de retorno: {e.returncode}")

modulo_desejado = "cryptography"  # Aqui onde você coloca o nome do módulo que deseja instalar automaticamente
instalar_modulo(modulo_desejado)

def gerarchave(): # /// chave de criptografia para segurança de interceptações \\\
    chave = Fernet.generate_key()
    return chave

def descriptografarfrase(chave, frasecriptografada): # /// descriptografar a frase \\\
    chavemestra = Fernet(chave)
    frasedescriptografada = chavemestra.decrypt(frasecriptografada).decode()
    return frasedescriptografada

def criptografarfrase(chave, frase): # /// criptografar a frase \\\
    chavemestra = Fernet(chave)
    frasecriptografada = chavemestra.encrypt(frase.encode())
    return frasecriptografada

'''
def contar_caracteres():
    entrada_texto = entry.get()    #Essa é a função da janela POP-UP mas era algo bem complexo e poderia dar xabu no code, estou estudando aos poucos!
    caracteres_label.config(text=f"Caracteres: {len(entrada_texto)}")
'''  

def salvararquivo(arquivo, chave, frasecriptografada): # /// salvar a chave e a frase criptografada em um único arquivo .txt \\\
    with open(arquivo, "w") as arquivo:
        arquivo.write("Chave de Criptografia:\n")
        arquivo.write(chave.decode() + "\n\n")
        arquivo.write("Frase Criptografada:\n")
        arquivo.write(frasecriptografada.decode())

#  /// A partir daqui o remetente e o destinatário escolhem se querem criptografar a mensagem ou então descriptografar a mensagem \\\

# ESCRITA 'DEV TINHO'
print("     _____          ___                                                         ___           ___           ___      ") 
print("    /  /::\        /  /\          ___                   ___       ___          /__/\         /__/\         /  /\     ")
print("   /  /:/\:\      /  /:/_        /__/\                 /  /\     /  /\         \  \:\        \  \:\       /  /::\    ")
print("  /  /:/  \:\    /  /:/ /\       \  \:\               /  /:/    /  /:/          \  \:\        \__\:\     /  /:/\:\   ")
print(" /__/:/ \__\:|  /  /:/ /:/_       \  \:\             /  /:/    /__/::\      _____\__\:\   ___ /  /::\   /  /:/  \:\  ")
print(" \  \:\ /  /:/ /__/:/ /:/ /\  ___  \__\:\           /  /::\    \__\/\:\__  /__/::::::::\ /__/\  /:/\:\ /__/:/ \__\:\ ")
print("  \  \:\  /:/  \  \:\/:/ /:/ /__/\ |  |:|          /__/:/\:\      \  \:\/\ \  \:\~~\~~\/ \  \:\/:/__\/ \  \:\ /  /:/ ")
print("   \  \:\/:/    \  \::/ /:/  \  \:\|  |:|          \__\/  \:\      \__\::/  \  \:\  ~~~   \  \::/       \  \:\  /:/  ")
print("    \  \::/      \  \:\/:/    \  \:\__|:|               \  \:\     /__/:/    \  \:\        \  \:\        \  \:\/:/   ")
print("     \__\/        \  \::/      \__\::::/                 \__\/     \__\/      \  \:\        \  \:\        \  \::/    ")
print("                   \__\/           ~~~~                                        \__\/         \__\/         \__\/     ")
      
while True:  # /// foi utilizado WHILE para que o usuário seja forçado em um loop a selecionar criptografar ou descriptografar. \\\
    
    maxCaracteres = 128 # /// Defina a quant. máxima de caracteres que pode ter a frase \\\
    
    acao = input("\nEscolha uma ação para a mensagem: \n\n1- criptografar \n2- descriptografar \n\nSua escolha: ").lower()
    
    if acao == "1":
        while True: # /// WHILE para verificar a quantidade de caracteres \\\
            frase = input("\nDigite a mensagem que deseja criptografar: ")
            if len(frase) <= maxCaracteres:  # /// checagem do tamanho da frase \\\
                print(f"\nMensagem com {len(frase)} caracteres. Restou {128-len(frase)} caracteres")
                break
            else:
                print(f"\nQuandidade de caracteres excedida: {len(frase)} total. Quantidade permitida: {maxCaracteres}")
                print(f"\nA quantidade de caracteres foi excedida em {len(frase)-128} a mais. Encurte a mensagem e tente novamente!")

        chave = gerarchave() # /// Gera a chave \\\

        frasecriptografada = criptografarfrase(chave, frase) # /// Criptografa a frase \\\

        nomearquivo = input("\nDigite o nome do arquivo onde deseja salvar a chave e a frase: ") # /// Aqui o usuário escolhe o nome do arquivo onde ficara armazenada a chave e a frase
        print("\n! LEMBRE-SE! GUARDE EM UM LOCAL SEGURO ESTE ARQUIVO POIS CONTÉM A CHAVE DE SEGURANÇA E A MENSAGEM !")
        caminhoarquivo = input("Digite o caminho onde deseja salvar o arquivo: ")
        
        if not os.path.exists(caminhoarquivo):
            os.makedirs(caminhoarquivo)

        caminhocompleto = os.path.join(caminhoarquivo, nomearquivo)
        
        salvararquivo(caminhocompleto, chave, frasecriptografada)
        print(f"\nChave e frase criptografada salvas no arquivo {caminhocompleto}")
        break

    elif acao == "2":
        
        caminhoarquivo = input("\nDigite o local do arquivo: ") # /// Solicita ao usuário que forneça o nome do arquivo \\\

        try:
            with open(caminhoarquivo, "r") as arquivo:
                    linhas = arquivo.read().splitlines()

            chave = linhas[1].encode()  #  /// A chave está na segunda linha do arquivo \\\
            frasecriptografada = linhas[-1].encode()  # /// A frase criptografada está na última linha do arquivo \\\
     
            chavedescriptografia = input("\nDigite a chave de descriptografia: ") # /// Solicita a chave de descriptografia \\\

            if chave == chavedescriptografia.encode():  # /// Descriptografa a frase e verifica se a chave é a correta para o arquivo \\\
                frasedescriptografada = descriptografarfrase(chave, frasecriptografada)
                print("\nFrase descriptografada:", frasedescriptografada)
                break
            else:
                print("\nChave de descriptografia incorreta. Não é possível descriptografar a frase.") # /// Erro de chave errada no arquivo \\\

        except FileNotFoundError:
            print(f"Arquivo '{caminhoarquivo}' não encontrado.") # /// Erro se não encontrar o arquivo correto \\\

    else:
        print("\nAção inválida. Escolha '1- criptografar' ou '2- descriptografar'.") # /// Else do loop para forçar a seleção de uma das opções \\\
