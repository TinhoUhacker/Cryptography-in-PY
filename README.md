# Cryptography-in-PY (EN-US)

This Python code implements a simple message encryption and decryption program using the cryptography.fernet library. The program allows the user to choose between encrypting a message or decrypting a previously encrypted message. The encryption key is automatically generated and saved together with the encrypted message in a text file.

Modules Used
• cryptography.fernet: Cryptography library used to implement message encryption and decryption.
• tkinter: Library for creating a graphical interface (not used in the current code).
• os: Module for interaction with the operating system (used to check the existence of the directory where the file will be saved).
• subprocess: Module for executing system commands (used to automatically install the cryptography module).

Functions
1. install_modulo(modulo): Function for automatic installation of a Python module. In this case, it is used to install the cryptography module.
2. generatekey(): Function to generate an encryption key using the cryptography.fernet module.
3. decryptphrase(key, encryptedphrase): Function to decrypt a message using the provided key.
4. encryptphrase(key, phrase): Function to encrypt a message using the provided key.
5. savefile(file, key, encrypted phrase): Function to save the key and encrypted message to a text file.

Variables
• maxCharacters: Maximum number of characters allowed in the message.

Program Flow
1. The program asks the user to choose between encrypting or decrypting a message.
2. If the user chooses to encrypt:
• Prompts for message input.
• Generates an encryption key.
• Encrypts the message.
• Prompts the user for a name for the file where the key and encrypted message will be saved.
• Saves the key and encrypted message to the specified file.
3. If the user chooses to decrypt:
• Requests the path of the file containing the key and the encrypted message.
• Reads the key and message from the file.
• Prompts the user for the decryption key.
• If the key is correct, decrypt the message and display it.

Comments
• The code contains a section related to using the tkinter module to create a graphical interface, but this part is commented and is not used in the current code.

# Cryptography-in-PY (PT-BR)
This Python code implements a simple message encryption and decryption program using the cryptography.fernet library. The program allows the user to choose between encrypting a message or decrypting a previously encrypted message. The encryption key is automatically generated and saved together with the encrypted message in a text file.

Módulos Utilizados
•	cryptography.fernet: Biblioteca de criptografia utilizada para implementar a criptografia e descriptografia da mensagem.
•	tkinter: Biblioteca para a criação de uma interface gráfica (não utilizada no código atual).
•	os: Módulo para interação com o sistema operacional (usado para verificar a existência do diretório onde o arquivo será salvo).
•	subprocess: Módulo para a execução de comandos do sistema (usado para instalar automaticamente o módulo cryptography).

Funções
1.	instalar_modulo(modulo): Função para instalação automática de um módulo Python. Neste caso, é usado para instalar o módulo cryptography.
2.	gerarchave(): Função para gerar uma chave de criptografia usando o módulo cryptography.fernet.
3.	descriptografarfrase(chave, frasecriptografada): Função para descriptografar uma mensagem usando a chave fornecida.
4.	criptografarfrase(chave, frase): Função para criptografar uma mensagem usando a chave fornecida.
5.	salvararquivo(arquivo, chave, frasecriptografada): Função para salvar a chave e a mensagem criptografada em um arquivo de texto.

Variáveis
•	maxCaracteres: Quantidade máxima de caracteres permitidos na mensagem.

Fluxo do Programa
1.	O programa solicita ao usuário escolher entre criptografar ou descriptografar uma mensagem.
2.	Se o usuário escolher criptografar:
•	Solicita a entrada da mensagem.
•	Gera uma chave de criptografia.
•	Criptografa a mensagem.
•	Solicita ao usuário um nome para o arquivo onde a chave e a mensagem criptografada serão salvas.
•	Salva a chave e a mensagem criptografada no arquivo especificado.
3.	Se o usuário escolher descriptografar:
•	Solicita o caminho do arquivo contendo a chave e a mensagem criptografada.
•	Lê a chave e a mensagem do arquivo.
•	Solicita ao usuário a chave de descriptografia.
•	Se a chave for correta, descriptografa a mensagem e a exibe.

Observações
•	O código contém uma seção relacionada ao uso do módulo tkinter para criar uma interface gráfica, mas essa parte está comentada e não é utilizada no código atual.


