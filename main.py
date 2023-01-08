from question_model import Question
from data import question_data

# q1 = Question(question_data[0], question_data[0])
# print(q1.text, q1.answer)
# print(question_data[1]["text"])
i = 0
question_bank = []
for _ in question_data:
    question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(question)
    i += 1

print(question_bank[1].text, question_bank[1]. answer)