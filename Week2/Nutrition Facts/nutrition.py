def main():
    # Dictionary containing the calorie information for fruits
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe":50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Prompt user to input a fruit (case-insensitively)
    fruit = input("Enter a fruit: ").lower()

    # Check if the input is a fruit and if yes, print its calorie count
    if fruit in fruit_calories:
        print("Calories:", fruit_calories[fruit])

if __name__ == "__main__":
    main()
