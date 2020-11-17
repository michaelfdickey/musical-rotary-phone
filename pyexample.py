import random

number_pool = list(range(1, 91))
computer_card = random.sample(number_pool, 15)
computer_card_sorted = sorted(computer_card)
player_card = random.sample(number_pool, 15)
player_card_sorted = sorted(player_card)


def display_cards():
    print("Computer card:\n")
    print(computer_card_sorted)
    print("====================================")
    print("Player card:\n")
    print(player_card_sorted)


def lotto_choice():
    choice = random.choice(number_pool)
    number_pool.remove(choice)
    return choice


def the_game():
    while number_pool:
        choice = lotto_choice()
        print("The random lotto is: " + str(choice))
        display_cards()
        cross_number = input("Do you want to cross out a number")
        cross_number.lower()
        if cross_number == "y":
            if choice in player_card_sorted:
                player_card_sorted.remove(choice)
            elif choice in computer_card_sorted:
                computer_card_sorted.remove(choice)
        if cross_number == "n":
            if choice in computer_card_sorted:
                computer_card_sorted.remove(choice)
            else:
                continue
    else:
        if len(player_card_sorted) == 0:
            print("Congratulations Player ! You won")
        elif len(computer_card_sorted) == 0:
            print("The computer have won, too bad !")
        else:
            print("It is a tie you both ran out of numbers, very straange !")


the_game()
