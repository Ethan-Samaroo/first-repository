def menu():
    print("===== TRIVIA GAME ===== \n \n"
          "1. Start Game \n"
          "2. View Categories\n"
          "3.View High Score\n"
          "4. Exit")
    option = input("Select an option: ")
    return option


categories = {"What's my name?": "General"}


def asking_question():
    points = 0
    choices = {"What's my name?": "A. Ethan \n B. Aidan \n C.Haseeb \n D.Hitesh"}
    answers = {"What's my name?": "A"}
    for question in choices:
        print(question)
        print(choices[question])
        answer = input("Choose an answer: ")
        if answer.upper() == answers[question]:
            points += 5
    print("Your score: " + str(points))
    return points


highscore = 0
option = menu()

while option != "4":
    if option == "1":
        score = asking_question()
        if highscore < score:
            print("NEW HIGH SCORE!!!")
            highscore = score
    if option == "2":
        for category in categories:
            print(categories[category])
    if option == "3":

        print("High Score: " + str(highscore))

    option = menu()
