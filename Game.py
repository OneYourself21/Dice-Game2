import random


def roll():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)

    total = dice_1 + dice_2

    if dice_1 == dice_2:
        dice_3 = random.randint(1,6)
        total += dice_3

    if total%2 == 0:
        total += 10

    elif total%2 == 1:
        total -= 5
        if total < 0:
            total = 0

    return total


def result(player1 , player2):
    if sum(player1.scores) > sum(player2.scores):
        return "One"
    elif sum(player1.scores) < sum(player2.scores):
        return "TWO"
    else:
        return "END GAME"


def duel(player1, player2, rolls):
    for i in range(rolls):
        player1.scores.append(roll())
        player2.scores.append(roll())

        print("Player 1 has gotten " + str(player1.scores[len(player1.scores) - 1]) + " in round " + str(i) + ".")
        print("Player 2 has gotten " + str(player2.scores[len(player2.scores) - 1]) + " in round " + str(i) + ".")

    return result(player1, player2)


def game(player1, player2):
    temp_result = duel(player1, player2, 5)

    if temp_result == "END GAME":
        print("END GAME!!!")
        while duel(player1.scores, player2.scores, 1) == "END GAME":
            pass

    return result(player1.scores, player2.scores)
