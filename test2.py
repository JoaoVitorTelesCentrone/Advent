import re

array = []
redLimit = 12
greenLimit = 13
blueLimit = 14

gamesList = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green' ]


def getGameAboveCount(string): 
    match = re.match(r"Game (\d+): (.+)", string)

    if match:
        game_number = match.group(1)
        games_string = match.group(2)
        
        # Use regular expression to split games by semicolon followed by optional whitespace
        games = re.split(r';\s*', games_string)
        
        print(f"Game Number: {game_number}")

        should_append = True  # Flag to determine whether to append the ID

        for game in games:
            matches = re.findall(r"(\d+) (blue|red|green)", game)
        
            for quantity, color in matches:
                print(f"Color: {color}, Quantity: {quantity}")
                if color == 'red' and int(quantity) > redLimit or color == 'green' and int(quantity) > greenLimit or color == 'blue' and int(quantity) > blueLimit:
                    print('Did not append')
                    should_append = False  # If any condition is met, set the flag to False
                    break  # Break out of the inner loop

        if should_append:
            id = int(game_number)
            print(f"Appending ID: {id}")
            array.append(id)

for value in gamesList: 
    getGameAboveCount(value)

print("Final Array:", array)
print("Sum of Array:", sum(array))
