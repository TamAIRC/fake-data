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
users_information = []
for _ in range(500000):
    user_information = {
        "age": round(random.uniform(15,50), 0),
        "major": fake.word(),
        "street address": fake.sentence(),
        "phone number": f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
    }
    users_information.append(user_information)
# print (questions)
json_object = json.dumps(users_information)
# Save data to a JSON file
with open(os.path.join(directory, 'users_information.json'), 'w', encoding='utf-8') as json_file:
    json_file.write(json_object)
