# Marvel Quiz Game

characters = ["Ant-Man", "Yondu Udonta", "Hawkeye", "Black Widow"]

quiz = {
    "Which Marvel character ran away from an orphanage and joined the Carson Carnival of Traveling Wonders?": 3,
    "Who has a talent for espionage?": 4,
    "Who shows an expert-level knowledge of electronics?": 1,
    "This character is not human, but rather a humanoid individual known as a Centaurian. Who belongs to this species?": 2
}

quizMarks = {
    "Which Marvel character ran away from an orphanage and joined the Carson Carnival of Traveling Wonders?": 5,
    "Who has a talent for espionage?": 4,
    "Who shows an expert-level knowledge of electronics?": 3,
    "This character is not human, but rather a humanoid individual known as a Centaurian. Who belongs to this species?": 6
}

quizResult = 0

print(f'\nAnswer the following quiz with one of the answers (Enter the number of Character):\n1. Ant-Man\n2. Yondu Udonta\n3. Hawkeye\n4. Black Widow\n\n')


def performQuiz():
    global quizResult
    global answers
    for ques in quiz.keys():
        print(ques)
        ans = int(input("Answer > "))
        if quiz[ques] == ans:
            quizResult += quizMarks[ques]
            print('Your Answer --> ', characters[ans-1])


def printRealAnswers():
    print('\n\nReal Answers for the Quiz are: -\n\n')
    for question in quiz.keys():
        print(f"{question}: {characters[quiz[question]-1]}")


performQuiz()

print("Result of quiz is ", quizResult, "points")

printRealAnswers()
