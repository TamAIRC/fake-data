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
users = []
for _ in range(500000):
    user = {
        "age": round(random.uniform(15,50), 0),
        "rank": round(random.uniform(1,10), 0),
        "major": fake.word(),
        "previous rank": round(random.uniform(1,10), 0),
    }
    users.append(user)
# print (questions)
json_object = json.dumps(users)
# Save data to a JSON file
with open(os.path.join(directory, 'users.json'), 'w', encoding='utf-8') as json_file:
    json_file.write(json_object)
