questionPrompts = (
    "1) What color are Apples?\n\n(a) Red\n(b) Blue\n(c) Purple\n(d) White\n\n",
    "2) What color are Bananas?\n\n(a) White\n(b) Orange\n(c) Yellow\n(d) Teal\n\n",
    "3) What color are Grape?\n\n(a) Pink\n(b) Purple\n(c) Orange\n(d) White\n\n",
)


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


questions = (
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b"),
)


def runTest(questions):
    correctAnswers = 0
    wrongAnswers = 0

    for question in questions:
        givenAnswer = ""

        while not givenAnswer or givenAnswer != "a" or "b" or "c" or "d":
            print(question.question)
            givenAnswer = input("Enter a letter choice: ")
            str(givenAnswer)
            givenAnswer = givenAnswer.lower()

            if not givenAnswer:
                print("\nPlease enter an answer.\n")
            elif givenAnswer not in "abcd":
                print("\nInvalid Answer. Please enter a valid letter choice.\n")
            elif len(givenAnswer) > 1:
                print("\nPlease enter only one letter choice.\n")
            elif givenAnswer in "abcd":
                if givenAnswer == question.answer:
                    correctAnswers += 1
                    break
                else:
                    wrongAnswers += 1
                    break

    score = correctAnswers / int(len(questions))

    formattedScore = str(round(float(score), 2)).lstrip("0.") + "%"
    formattedCorrectAnswers = str(correctAnswers)
    formattedWrongAnswers = str(wrongAnswers)

    print(
        "Thanks for taking the quiz!\nYour score: "
        + formattedScore
        + ".\nCorrect Answers: "
        + formattedCorrectAnswers
        + ".\nIncorrect Answers: "
        + formattedWrongAnswers
        + "."
    )


runTest(questions)