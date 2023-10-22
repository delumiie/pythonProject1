from random import randint


def play_casino_game(selected_slot, bet):
    win_slot = randint(1, 31)
    if selected_slot == win_slot:
        return "win", bet * 2
    else:
        return "lose", -bet
