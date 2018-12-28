from Questions import Question          # Goal this weekend create multi choice game

question_prompts = [                                                        # Array
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
    "what color are Grapes?\n(a) Green\n(b) Purple\n(c) Red\n\n",

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)