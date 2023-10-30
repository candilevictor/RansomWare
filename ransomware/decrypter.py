import os
import pyaes

# Função para ler a chave de descriptografia do arquivo
def read_decryption_key():
    with open('key.rans', 'r') as key_file:
        return key_file.read()

# Abrir o arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Solicitar a chave de descriptografia do usuário
key = input("Insira a chave de descriptografia: ")  # A chave é fornecida pelo usuário

# Realizar a descriptografia
aes = pyaes.AESModeOfOperationCTR(key.encode())
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar um novo arquivo descriptografado
new_file_name = 'teste.txt'
with open(new_file_name, 'wb') as new_file:
    new_file.write(decrypt_data)

print("Arquivo descriptografado com sucesso.")

# Remover o arquivo criptografado
os.remove('key.rans')
