print("Welcome to Manga Recommender for readers!🙂")
print("Answer a few questions to find your next read.")
genre_choice = input("What genre do you like? (action, romance, fantasy): ")

if genre_choice == "action":

    chapter = input("How long is the manga you want to read? (short, medium, long): ")
    if chapter == "short":
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("Sorry, we don't have any recommendation 🥺")
        
        else:
            print("We recommend you to read \"Goodbye, Eri👋🏻\"")
            print("Enjoy Reading!😊")

    elif chapter == "medium":
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"Akame ga Kill💥\"")
            print("Enjoy Reading!😊")

        else:
            print("We recommend you to read \"Hell's Paradise🔥\"")
            print("Enjoy Reading!😊")

    else:
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"Attack on Titan🧍🏻‍♂️\"")
            print("Enjoy Reading!😊")

        else:
            print("We recommend you to read \"My Hero Academia🦸🏻\"")
            print("Enjoy Reading!😊")

elif genre_choice == "romance":

    chapter = input("How long is the manga you want to read? (short, medium, long): ")
    if chapter == "short":
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"Last Game 🎮\"")
            print("Enjoy Reading!😊")
        
        else:
            print("We recommend you to read \"Look Back 👁️\"")
            print("Enjoy Reading!😊")

    elif chapter == "medium":
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"A Silent Voice 😶\"")
            print("Enjoy Reading!😊")

        else:
            print("We recommend you to read \"Blue Flag 🔵🏳️\"")
            print("Enjoy Reading!😊")

    else:
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"Kaguya-Sama:Love is War💘\"")
            print("Enjoy Reading!😊")

        else:
            print("We recommend you to read \"Horimiys👩🏻‍❤️‍🧑🏻\"")
            print("Enjoy Reading!😊")

elif genre_choice == "fantasy":

    chapter = input("How long is the manga you want to read? (short, medium, long): ")
    if chapter == "short":
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("Sorry, we don't have any recommendation 🥺")
        
        else:
            print("We recommend you to read \"Demon Slayer: Kimetsu no Yaiba😈\"")
            print("Enjoy Reading!😊")

    elif chapter == "medium":
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"The Promised Neverland 🏝️\"")
            print("Enjoy Reading!😊")

        else:
            print("We recommend you to read \"Tokyo Revengers🥷🏻\"")
            print("Enjoy Reading!😊")

    else:
        time = input("Which timeline? (2010s, 2020s): ")
        if time == "2010s":
            print("We recommend you to read \"Tokyo Ghoul 👻\"")
            print("Enjoy Reading!😊")

        else:
            print("We recommend you to read \"Jujutsu Kaisen\"")
            print("Enjoy Reading!😊")

else:
    print("Sorry, we don't have any recommendation for that genre 😔")