import json
from faker import Faker
import random
import os
import hashlib

# Create the directory if it doesn't exist
directory = 'data-fake/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate data using Faker
fake = Faker('vi_VN')
questions = []
Answers = []

for _ in range(500000):
    options = [fake.sentence() for _ in range(4)]
    question_sentence = fake.sentence()
    print("question", _)
    question = {
        # Convert hash to string
        "question_detail": question_sentence,
        "answer_options": options,
        "correct_answer": random.randint(1, 4),
        "major": fake.word(),
        "difficulty": round(random.uniform(1, 10), 0),
        "rating": round(random.uniform(1, 5), 1),
        "reward": random.choice([10, 100, 200, 300, 500, 1000]),
    }
    questions.append(question)
# print (questions)
json_object = json.dumps(questions)
# Save data to a JSON file
with open(os.path.join(directory, 'questions.json'), 'w', encoding='utf-8') as json_file:
    json_file.write(json_object)
