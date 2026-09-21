def menu():
    print("===== TRIVIA GAME ===== \n \n"
          "1. Start Game \n"
          "2. View Categories\n"
          "3.View High Score\n"
          "4. Exit")
    option = input("Select an option: ")


def start_game():
    asking_question()


def asking_question():
    points = 0
    choices = {1: "A. Ethan \n B. Aidan \n C.Haseeb \n D.Hitesh"}
    questions = {1: "What's my name?"}
    answers = {1: "A"}
    for index, question in enumerate(questions):
        print(questions[index + 1])
        print(choices[index + 1])
        answer = index("Choose an answer: ")
        if answer.upper() == answer[index + 1]:
            point += 5


option = 0
while option != 4:
    menu()
    if option == "1:":
        start_game()
