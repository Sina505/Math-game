# Math Practice Game

A small terminal game for practicing mental math. It throws random questions at you and you try to answer them as quickly as you can. Right answers add points and wrong ones take points away.

## How it works

When you start, the game asks for three things:

1. The lowest number of the range
2. The highest number of the range
3. The mode

Both numbers in every question are picked from your range. For example, a range of 2 to 10 gives you questions like `7 + 3 = ?` or `4 * 9 = ?`. Both range numbers have to be 1 or more, and the highest can't be smaller than the lowest.

There are three modes. It doesn't matter if you type them in capital or small letters.

| Mode   | Operations         | Points per answer |
|--------|--------------------|-------------------|
| easy   | `+` `-`            | +1 / -1           |
| medium | `*` `**` (power)   | +2 / -2           |
| hard   | `+` `-` `*` `**`   | +2 / -2           |

If you get a question wrong, the game shows you the correct answer so you can learn from it. If you type something that isn't a number, it just asks again. To stop playing, type `q` instead of an answer and you'll see your final score.

## Running it

You only need Python 3, no extra libraries:

    python math_game.py

## Example

    pls enter the lowest number of the range: 2
    pls enter the highest number of the range: 10
    Easy, Medium, Hard
    choose the mode: easy
    7 + 3 = ?
    your answer is (q to quit): 10
    ...Correct...
    your score is 1

## Tips

- Keep the range small in medium and hard mode. Powers grow really fast, so something like `30 ** 20` is not much fun to calculate by hand.
- Easy mode can give negative answers (like `3 - 8`), so don't forget the minus sign.

## Known issues

- The score can go negative if you get a lot of answers wrong.

## About this project

I made this to practice Python (functions, loops, dictionaries, the `random` module) and to get a bit faster at calculations at the same time. Things I'd like to add later: a fixed number of questions per round, a timer, and a high score.