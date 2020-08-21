def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])


print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')
print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))
print_hand(player_hand, player_name)