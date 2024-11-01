## Foi avisado que os textos inseridos seriam sem espaços em branco, sem acento e sem letras diferentes das 25; Portanto, funções baseadas nessas instruções:

letter_alphabet = {
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e',
  5: 'f',
  6: 'g',
  7: 'h',
  8: 'i',
  9: 'j',
  10: 'k',
  11: 'l',
  12: 'm',
  13: 'n',
  14: 'o',
  15: 'p',
  16: 'q',
  17: 'r',
  18: 's',
  19: 't',
  20: 'u',
  21: 'v',
  22: 'w',
  23: 'x',
  24: 'y',
  25: 'z'
}

frequencyAnalysis = {
  'a': 13.9,
  'b': 1.0,
  'c': 4.4,
  'd': 5.4,
  'e': 12.2,
  'f': 1.0,
  'g': 1.2,
  'h': 0.8,
  'i': 6.9,
  'j': 0.4,
  'k': 0.1,
  'l': 2.8,
  'm': 4.2,
  'n': 5.3,
  'o': 10.8,
  'p': 2.9,
  'q': 0.9,
  'r': 6.9,
  's': 7.9,
  't': 4.9,
  'u': 4.0,
  'v': 1.3,
  'w': 0.0,
  'x': 0.3,
  'y': 0.0,
  'z': 0.4
}

# Invertendo o objeto para ter acesso pela letra
number_alphabet = {letter_alphabet[key]: key for key in letter_alphabet.keys()}

def shift_cypher(number_shift, text):
    crypting_number = []
    crypting = ''
    # Convertendo texto para números com deslocamento
    for char in text:
        index = number_alphabet[char.lower()]
        crypting_number.append(index + number_shift)
    # Convertendo números criptografados para letras
    for number_crypto in crypting_number:
        number_alpha = number_crypto % 26  # Utilizando módulo para lidar com deslocamentos
        crypting += letter_alphabet[number_alpha]
    return crypting

def brute_force(text):
    amount_letters = 26
    for i in range(amount_letters):  # Iterando sobre o número de letras no alfabeto
        text_decrypt = ''
        for char in text:
            number_text = number_alphabet[char] - i  # Decrementando o deslocamento
            if number_text < 0:
                number_text += amount_letters
            text_decrypt += letter_alphabet[number_text]
        print(f'Tamanho do deslocamento: {i}, {text_decrypt}')

# Calcula a frequência do texto dado
def frequency_analysis(text):
    counts = {}
    total_chars = 0

    for char in text.lower():
        if char.isalpha():
            total_chars += 1
            if char in counts:
                counts[char]['count'] += 1
            else:
                counts[char] = {'count': 1, 'frequency': 0.0}
    for char, data in counts.items():
        data['frequency'] = data['count'] / total_chars
    return counts

# Primeira função de decriptografia de texto pela frequência (pode ser usada essa ou a generate_permutations)
def transform_text_by_frequency(text):
    counts = frequency_analysis(text)

    # Ordena as letras do texto por frequência em ordem decrescente
    sorted_text_freq = sorted(counts.items(), key=lambda x: -x[1]['frequency'])

    # Ordena o frequencyAnalysis por valor em ordem decrescente
    sorted_ref_freq = sorted(frequencyAnalysis.items(), key=lambda x: -x[1])

    char_map = {
        char: sorted_ref_freq[i][0]
        for i, (char, _) in enumerate(sorted_text_freq)
    }
    new_text = ''.join(char_map.get(char, char) for char in text.lower())
    return new_text




def get_replacement_options(text):
    counts = frequency_analysis(text)
    sorted_ref_freq = sorted(frequencyAnalysis.items(), key=lambda x: -x[1])
    sorted_text_freq = sorted(counts.items(), key=lambda x: -x[1]['frequency'])

    options_map = {}
    for i, (char, data) in enumerate(sorted_text_freq):
        # Seleciona duas letras com as maiores frequências possíveis
        options = [sorted_ref_freq[j % len(sorted_ref_freq)][0] for j in range(i, i + 2)]
        options_map[char] = options

    print("Mapa de opções de substituição:", options_map)
    generate_permutations(text, options_map)
    return options_map

# Função que imprime a com a primeira opçao de entrada e com a segunda depois.
# Segunda função de decriptografia de texto pela frequência
def generate_permutations(text):
    options_map = get_replacement_options(text)
    # Substitui usando a primeira opção
    first_option_text = ''.join(options_map.get(char, [char])[0] for char in text.lower())
    print("\nTexto com a primeira opção:")
    print(first_option_text)

    # Substitui usando a segunda opção (se houver)
    second_option_text = ''.join(
        options_map.get(char, [char])[1] if len(options_map.get(char, [])) > 1 else options_map.get(char, [char])[0]
        for char in text.lower()
    )
    print("\nTexto com a segunda opção:")
    print(second_option_text)
      
# A vantagem da força bruta é quando se sabe qual é o metodo utilizado porém ela possui uma complexidade de O(n⋅m) onde depende do comprimento do texto e do número de deslocamentos, o que pode ser demorado para textos maiores.
# Já a análise de frequência é melhor para textos longos onde a frequencia pode ser comparada com a tabela (retirada pela referência da professora) ela possui O(n+klogk) de complexidade.
