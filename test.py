myList = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
    # Add more card data as needed
]

def calculate_wins(cards_data):
    wins = {}

    for i, card_data in enumerate(cards_data):
        wins[i + 1] = []  # Initialize an empty list for each card

        card_numbers = [int(num) for num in re.findall(r'\d+', card_data)]

        for j, other_card_data in enumerate(cards_data[i + 1:], start=i + 2):
            other_card_numbers = [int(num) for num in re.findall(r'\d+', other_card_data)]

            matching_numbers = set(card_numbers) & set(other_card_numbers)

            if len(matching_numbers) > 0:
                # Calculate the number of copies won based on the matching numbers
                copies_won = min(len(matching_numbers), len(other_card_numbers) - len(matching_numbers))
                wins[i + 1].append((j + 1, copies_won))

    return wins

def print_wins(wins, cards_data):
    for card, copies in wins.items():
        if copies:
            print(f'Card {card} has:')
            for other_card, copies_won in copies:
                if other_card <= len(cards_data):
                    print(f'  - {copies_won} copy{"s" if copies_won > 1 else ""} of Card {other_card}')
                else:
                    print(f'  - {copies_won} copy{"s" if copies_won > 1 else ""} of a non-existing Card')

# Example usage
# Example usage
import re

wins = calculate_wins(myList)
print_wins(wins)
