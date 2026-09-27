def game_outcome(your_score, opponent_score):
    if your_score > opponent_score:
        return "You win!"
    elif your_score < opponent_score:
        return "You lose!"
    elif your_score == opponent_score:
        return "Tie game!"
    elif your_score < 0 and opponent_score < 0
        return "Invalid score. Scores cannot be negative."


def main():
    your_score = int(input("enter your score: "))
    opponent_score = int(input("enter your opponents score: "))
    result = game_outcome(your_score, opponent_score)
    print(result)

main()

