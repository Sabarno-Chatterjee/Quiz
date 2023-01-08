from question_model import Question
from data import question_data

# q1 = Question(question_data[0], question_data[0])
# print(q1.text, q1.answer)
# print(question_data[1]["text"])
# i = 0
# question_bank = []
# for question in question_data:
#     new_question = Question(question_data[i]["text"], question_data[i]["answer"])
#     question_bank.append(new_question)
#     i += 1
#
# print(question_bank[1].text, question_bank[1]. answer)
# print(question_bank)

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)