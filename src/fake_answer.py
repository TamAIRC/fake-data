import json
import pymongo
from pymongo import MongoClient
from faker import Faker
import random
import os
# Create the directory if it doesn't exist
directory = 'data-fake/'
if not os.path.exists(directory):
    os.makedirs(directory)
# Generate data using Faker
fake = Faker('vi_VN')
answers = []
for _ in range(500000):
    options = [fake.sentence() for _ in range(4)]
    answer = random.choice(options)
    answer = {
        "answer": answer
    }
    answers.append(answer)
# print (questions)
json_object = json.dumps(answers)
# Save data to a JSON file
with open(os.path.join(directory, 'questions.json'), 'w', encoding='utf-8') as json_file:
    json_file.write(json_object)
