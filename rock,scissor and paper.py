import random

def play():
    user = input("what is your choice? 'r' for rock,'s' for scissors and 'p' for paper:")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won!'
    return 'You lost'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') and (player == 'p' and opponent == 'r') and (player == 'p' and opponent == 's'):
        return True

print(play())
