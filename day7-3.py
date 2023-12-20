cartas_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

test = [
    '32T3K 765',
    '8233K 764',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]


def process_and_compare(test_data):
    hands_data = []

    for hand_data in test_data:
        hand, bid = hand_data.split()  
        hand_array = list(hand)        
        bid_value = int(bid)           

        hands_data.append({
            'hand': tuple(hand_array),  
            'bid': bid_value
        })

    
    for i in range(len(hands_data) - 1):
        hand1 = hands_data[i]['hand']
        hand2 = hands_data[i + 1]['hand']

        # order this hands

    return hands_data

strenght = {}

processed_data = process_and_compare(test)

for data in processed_data:
    print(f'Hand: {data["hand"]}, Bid: {data["bid"]}')
