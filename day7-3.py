cartas_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
# Lista de testes
test = [
    '32T3K 765',
    '8233K 764',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]

# Função para quebrar cada mão, extrair o valor do bid e realizar comparações
def process_and_compare(test_data):
    hands_data = []

    for hand_data in test_data:
        hand, bid = hand_data.split()  # Divide a mão e o bid
        hand_array = list(hand)        # Converte a mão para uma lista de caracteres
        bid_value = int(bid)           # Converte o bid para um número inteiro

        hands_data.append({
            'hand': tuple(hand_array),  # Converte a mão para uma tupla
            'bid': bid_value
        })

    # Realiza comparações desejadas
    for i in range(len(hands_data) - 1):
        hand1 = hands_data[i]['hand']
        hand2 = hands_data[i + 1]['hand']

        compare_hands(hand1, hand2)

    return hands_data

# Função para comparar duas mãos com base nas regras especificadas
def compare_hands(hand1, hand2):
    order_of_hands = ['Five of a Kind', 'Four of a Kind', 'Full House', 'Three of a Kind', 'Two Pair', 'Pair', 'High Card']

    for order in order_of_hands:
        if order in strenght[hand1] and order in strenght[hand2]:
            # Both hands have the same category, compare their values
            value1 = get_hand_value(hand1, order)
            value2 = get_hand_value(hand2, order)

            if value1 > value2:
                print(f"The hand {hand1} is greater than {hand2}.")
                break
            elif value1 < value2:
                print(f"The hand {hand2} is greater than {hand1}.")
                break
        elif order in strenght[hand1]:
            print(f"The hand {hand1} is greater than {hand2}.")
            break
        elif order in strenght[hand2]:
            print(f"The hand {hand2} is greater than {hand1}.")
            break

# Função auxiliar para obter o valor da mão com base na categoria
def get_hand_value(hand, category):
    # Adicione lógica para calcular o valor da mão com base na categoria especificada
    # Neste exemplo, está retornando a soma dos valores das cartas na mão
    return sum(cartas_dict[card] for card in hand)

# Dicionário para armazenar a força de cada mão
strenght = {}

# Processa os dados de teste e realiza comparações
processed_data = process_and_compare(test)

# Exibe os resultados
for data in processed_data:
    print(f'Hand: {data["hand"]}, Bid: {data["bid"]}')
