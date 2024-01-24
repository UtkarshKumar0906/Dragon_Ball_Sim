import random

class Character:
    def __init__(self, name, health, power_level, speed):
        self.name = name
        self.health = health
        self.base_power_level = power_level
        self.power_level = power_level
        self.speed = speed
        self.can_attack = True  # New attribute to track if the character can attack in the current turn

    def attack(self, opponent):
        damage = self.power_level * 2
        if random.uniform(0, 1) > opponent.speed:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} and deals {damage} damage!")
        else:
            print(f"{opponent.name} evaded {self.name}'s attack!")

        self.can_attack = False  # Set to False after attacking

    def display_status(self):
        print(f"{self.name} - Health: {self.health}, Power Level: {self.power_level}, Speed: {self.speed}")

    def increase_power_level(self):
        self.power_level += 100
        print(f"{self.name}'s power level has increased! New Power Level: {self.power_level}")
        self.can_attack = False  # Set to False after increasing power level


def choose_character():
    print("Choose your character:")
    for i, character in enumerate(characters, 1):
        print(f"{i}. {character.name}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen character: "))
            if 1 <= choice <= len(characters):
                user_character = characters[choice - 1]
                characters.remove(user_character)  # Remove the chosen character from the list
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nChoose your opponent:")
    for i, character in enumerate(characters, 1):
        print(f"{i}. {character.name}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen opponent: "))
            if 1 <= choice <= len(characters):
                opponent = characters[choice - 1]
                return user_character, opponent
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def opponent_power_up(opponent):
    # Randomly determine if the opponent will power up
    if random.choice([True, False]):
        opponent.increase_power_level()
        print(f"{opponent.name} powered up! New Power Level: {opponent.power_level}")
    else:
        print(f"{opponent.name} decided not to power up in this round.")


def fight(user_character, opponent):
    round_count = 1
    while user_character.health > 0 and opponent.health > 0:
        print(f"\n--- Round {round_count} ---")
        user_character.display_status()
        opponent.display_status()

        # Give the player the option to increase power level
        increase_power = input("Do you want to increase your power level? (yes/no): ").lower()
        if increase_power == 'yes':
            user_character.increase_power_level()
        else:
            user_character.can_attack = True  # If not increasing power level, the character can attack

        # Opponent randomly decides to power up or not
        opponent_power_up(opponent)

        # User's character attacks opponent if allowed
        if user_character.can_attack:
            user_character.attack(opponent)
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated! {user_character.name} wins!")
                break

        # Opponent attacks user's character
        opponent.attack(user_character)
        if user_character.health <= 0:
            print(f"{user_character.name} has been defeated! {opponent.name} wins!")
            break

        round_count += 1


if __name__ == "__main__":
    characters = [
        Character("Goku", 1000, 80, 0.9),
        Character("Vegeta", 950, 75, 0.8),
        Character("Piccolo", 800, 70, 0.7),
        Character("Gohan", 850, 65, 0.8),
        Character("Frieza", 900, 85, 0.9),
        Character("Cell", 950, 90, 0.85),
        Character("Majin Buu", 1200, 100, 0.75),
        Character("Trunks", 850, 75, 0.8),
        Character("Krillin", 750, 60, 0.6),
        Character("Tien", 700, 55, 0.7),
        Character("Yamcha", 650, 50, 0.8),
        Character("Android 18", 900, 80, 0.9),
        Character("Broly", 1100, 95, 0.7),
        Character("Beerus", 1500, 120, 0.95),
        Character("Whis", 2000, 150, 0.98),
        Character("Hit", 1200, 110, 0.8),
        Character("Jiren", 1800, 130, 0.99),
        Character("Pan", 800, 70, 0.7),
        Character("Master Roshi", 700, 60, 0.6),
        Character("Chi-Chi", 600, 55, 0.5),
    ]

    user_character, opponent = choose_character()
    print(f"\nYou've chosen {user_character.name}!")
    print(f"You'll be fighting against {opponent.name}!\n")

    fight(user_character, opponent)
