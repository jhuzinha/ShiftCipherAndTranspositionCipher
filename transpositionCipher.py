from itertools import permutations

def get_key_order(key):
    # Ordena a chave e retorna os índices ordenados
    key_list = list(key)
    order = sorted(range(len(key_list)), key=lambda k: key_list[k])
    return order

def transposition_cipher(message, key):
    message = message.replace(" ", "")
    num_columns = len(key)
    num_rows = (len(message) + num_columns - 1) // num_columns

    # Criar matriz de transposição
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0

    # Preencher matriz linha a linha
    for i in range(num_rows):
        for j in range(num_columns):
            if index < len(message):
                matrix[i][j] = message[index]
                index += 1

    # Obter a ordem da chave
    key_order = get_key_order(key)
    
    # Montar texto cifrado pela ordem das colunas
    encrypted_message = ""
    for column_index in key_order:
        for row in range(num_rows):
            if matrix[row][column_index] != '':
                encrypted_message += matrix[row][column_index]

    return encrypted_message

def transposition_decipher(encrypted_message, key):
    num_columns = len(key)
    num_rows = (len(encrypted_message) + num_columns - 1) // num_columns

    # Obter ordem da chave
    key_order = get_key_order(key)
    
    # Criar matriz para decifração
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0

    # Calcular quantos caracteres em cada coluna
    full_columns = len(encrypted_message) % num_columns
    characters_per_column = [num_rows] * full_columns + [num_rows - 1] * (num_columns - full_columns)
    
    # Preencher matriz coluna a coluna de acordo com a ordem da chave
    for column_index in key_order:
        for row in range(characters_per_column[column_index]):
            if index < len(encrypted_message):
                matrix[row][column_index] = encrypted_message[index]
                index += 1

    # Ler matriz linha a linha para decifrar
    decrypted_message = ""
    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] != '':
                decrypted_message += matrix[i][j]

    return decrypted_message

# Example of usage
message = "CIFRA DE TRANSPOSICAO TUDO CERTO"
key = "TEAMAMOS"
encrypted_message = transposition_cipher(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = transposition_decipher(encrypted_message, key)
print("Decrypted Message:", decrypted_message)

# Função para tentar decifrar usando o tamanho da chave
def attempt_decrypt(encrypted_message, num_columns):
    num_rows = (len(encrypted_message) + num_columns - 1) // num_columns
    full_columns = len(encrypted_message) % num_columns
    characters_per_column = [num_rows] * full_columns + [num_rows - 1] * (num_columns - full_columns)

    # Criar matriz para decifração
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0

    # Preencher matriz coluna a coluna
    for column in range(num_columns):
        for row in range(characters_per_column[column]):
            if index < len(encrypted_message):
                matrix[row][column] = encrypted_message[index]
                index += 1

    # Testar todas as permutações possíveis de colunas
    for permutation in permutations(range(num_columns)):
        decrypted_message = ""
        for row in range(num_rows):
            for column in permutation:
                if matrix[row][column] != '':
                    decrypted_message += matrix[row][column]

        # Verificar se o texto decifrado faz sentido (contém palavras conhecidas)
        if readable_text(decrypted_message):
            print(f"Possible decryption with permutation {permutation}: {decrypted_message}")

# Função para determinar se um texto é legível (heurística simples)
def readable_text(text):
    common_words = ["DE", "O", "A", "E", "OS", "AS", "DA", "DO"]
    for word in common_words:
        if word in text:
            return True
    return False

# Tentativa de decifrar com diferentes números de colunas
for num_columns in range(2, len(encrypted_message)):
    print(f"Trying to decrypt with {num_columns} columns...")
    attempt_decrypt(encrypted_message, num_columns)
