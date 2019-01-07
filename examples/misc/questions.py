class Question:

    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

q1 = Question("What is the answer?", 42, [5, 3, 42, 75])
q2 = Question("Pick a color", "blue", ["red", "orange", "yellow", "green", "blue", "purple"])
q3 = Question("What day is it?", "Monday", ["Monday", "Tuesday", "Wednesday"])

questions = [q1, q2, q3]

current_question = questions.pop(0)

print(f"Question: {current_question.question}")
print(f"Choices: {current_question.choices}")
print(f"Answer: {current_question.answer}")