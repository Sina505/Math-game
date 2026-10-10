import random

MODES = {
    "easy": {"symbols": ["+", "-"], "points": 1},
    "medium": {"symbols": ["*", "**"], "points": 2},
    "hard": {"symbols": ["+", "-", "*", "**"], "points": 2},
}


def ask_number(message, minimum=1):
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("please enter a valid number")
            continue
        if value < minimum:
            print(f"the number should be {minimum} or more")
            continue
        return value


def ask_mode():
    while True:
        choice = input("Easy, Medium, Hard\nchoose the mode: ").strip().lower()
        if choice in MODES:
            return choice
        print("you should just choose these modes")


def calculate(num_1, symbol, num_2):
    if symbol == "+":
        return num_1 + num_2
    if symbol == "-":
        return num_1 - num_2
    if symbol == "*":
        return num_1 * num_2
    return num_1 ** num_2


def play(mode, low, high):
    score = 0
    points = MODES[mode]["points"]
    symbols = MODES[mode]["symbols"]

    while True:
        num_1 = random.randint(low, high)
        num_2 = random.randint(low, high)
        symbol = random.choice(symbols)

        print(f"{num_1} {symbol} {num_2} = ?")
        answer = input("your answer is (q to quit): ").strip().lower()

        if answer == "q":
            print(f"game over, your final score is {score}")
            break

        try:
            answer = int(answer)
        except ValueError:
            print("please enter a valid number")
            continue

        correct_answer = calculate(num_1, symbol, num_2)

        if answer == correct_answer:
            score += points
            print("...Correct...")
        else:
            score -= points
            print("its not correct")
            print(f"the correct answer is {correct_answer}")
        print(f"your score is {score}")


def main():
    low = ask_number("pls enter the lowest number of the range: ")
    high = ask_number("pls enter the highest number of the range: ", minimum=low)
    mode = ask_mode()
    play(mode, low, high)


if __name__ == "__main__":
    main()
