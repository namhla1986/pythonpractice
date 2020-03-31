from questions import Questions
question_prompts = [
    "How do you solve an argument in the classroom?\n a) Scream at your colleague\n b) Talk rationally c)\n Walk away\n",
    "Can you teach writing to the children?\n a) Yes, in secret\n b) No, it is illegal \n c) Yes, in moderation\n",
    "What do you do when you are late?\n a) Keep quiet\n b) Panic\n c) Text a head teacher\n"
]

question = [
    Questions(question_prompts[0], "b"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions: