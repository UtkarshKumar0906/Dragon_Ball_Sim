class Character:
    def __init__(self, name, health, power_level):
        self.name = name
        self.health = health
        self.power_level = power_level

    def attack(self, opponent):
        damage = self.power_level * 2
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage!")

    def display_status(self):
        print(f"{self.name} - Health: {self.health}, Power Level: {self.power_level}")


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


def fight(user_character, opponent):
    round_count = 1
    while user_character.health > 0 and opponent.health > 0:
        print(f"\n--- Round {round_count} ---")
        user_character.display_status()
        opponent.display_status()

        # User's character attacks opponent
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
        Character("Goku", 1000000, 9000),
        Character("Broly", 1200000, 8000),
        Character("Vegeta", 900000, 7000),
        Character("Frieza", 800000, 7500),
        Character("Gohan",800000,6000),
    ]

    user_character, opponent = choose_character()
    print(f"\nYou've chosen {user_character.name}!")
    print(f"You'll be fighting against {opponent.name}!\n")

    fight(user_character, opponent)
