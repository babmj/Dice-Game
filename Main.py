import random

# -----------------------------
# Die class
# -----------------------------
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        # returns a random number between 1 and number of sides
        return random.randint(1, self.sides)

# -----------------------------
# DiceGame class
# -----------------------------
class DiceGame:
    def __init__(self):
        # create two Die objects
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        # determine result based on total
        if total in [7, 11]:
            return "Win"
        elif total in [2, 3, 12]:
            return "Lose"
        else:
            return "Roll Again"

    def play_round(self):
        # roll both dice
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)
        # return 4 values for testing
        return roll1, roll2, total, result

# -----------------------------
# main function (menu)
# -----------------------------
def main():
    game = DiceGame()
    print("Welcome to the Dice Game!")

    while True:
        print("\nMenu:")
        print("1. Play a round")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            roll1, roll2, total, result = game.play_round()
            print(f"\nYou rolled {roll1} and {roll2}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == "2":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

# -----------------------------
# run main if file is executed
# -----------------------------
if __name__ == "__main__":
    main()
