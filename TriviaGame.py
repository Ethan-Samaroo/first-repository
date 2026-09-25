def menu() -> str:
    option = 0
    print("===== TRIVIA GAME ===== \n \n"
          "1. Start Game \n"
          "2. View Categories\n"
          "3.View High Score\n"
          "4. Exit")
    try:
        option = int(input("Select an option: "))
    except ValueError:
        print("Please type a number!")
    return option


categories = {"General", "Science", "History"}


def asking_question() -> int:
    points = 0
    questions = ("What's my name?",)
    choices = ("A. Ethan \n B. Aidan \n C.Haseeb \n D.Hitesh",)
    answers = ("A",)
    for index, question in enumerate(questions):
        print(question)
        print(choices[index])
        answer = input("Choose an answer: ")
        if answer.upper() == answers[index]:
            points += 5
    print("Your score: " + str(points))
    return points


highscore = 0
option = menu()

while option != 4:
    if option == 1:
        score = asking_question()
        if highscore < score:
            print("NEW HIGH SCORE!!!")
            highscore = score
    if option == 2:
        for category in categories:
            print(category)
    if option == 3:

        print("High Score: " + str(highscore))

    option = menu()
