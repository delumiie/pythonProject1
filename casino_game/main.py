from casino_game.casino_logic import play_casino_game
from decouple import config

initial_money = int(config('MY_MONEY', default=1000))

print(f"Welcome to Casino game! Your initial capital: ${initial_money}")

while initial_money > 0:
    slot = int(input("Choose a slot (1-30) for the bet: "))
    while True:
        bet = int(input("Bet amount: $"))
        if bet > initial_money:
            print(f"You don't have enough money!! Your current capital: ${initial_money}")
            continue
        else:
            break

    result, money_change = play_casino_game(slot, bet)
    initial_money += money_change

    if result == "win":
        print(f"You won ${money_change}! Your current capital: ${initial_money}")
        continue
    else:
        print(f"You lose ${abs(money_change)}. Your current capital: ${initial_money}")

    if initial_money <= 0:
        print("You don't have money!! Game is over.")
        break

    play_again = input("Do you want to play more? (yes/no): ").lower()
    if play_again != "yes":
        break

if initial_money > 1000:
    print("Congratulations, you are winning!")
else:
    print("You lost. Good luck next time!")
