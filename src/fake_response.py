import json
from faker import Faker
import random
import os
import hashlib
import pymongo
from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DTU-test']  # Choose your database
users_collection = db['User']
questions_collection = db['Question']
response_collection = db['Response']

# Create the directory if it doesn't exist
directory = 'data-fake/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Fetch existing users and questions from MongoDB
existing_users = list(users_collection.find())
existing_questions = list(questions_collection.find())

# Print the length of existing_users
# print("Number of existing users:", len(existing_users))

# Generate data using Faker for responses
fake = Faker('vi_VN')
responses = []

for _ in range(len(existing_users)):  # Assuming 500 responses
    user = random.choice(existing_users)
    user_id = user['_id']
    print(_ ,'user_id: ', user_id)
    
    num_questions = 10
    question_ids_selected = [random.choice(existing_questions)['_id'] for _ in range(num_questions)]
    answer_ids_selected = [random.randint(1, 4) for _ in range(num_questions)]
    complete_time = fake.date_time_this_year(before_now=True, after_now=False)
    time_for_question = [random.randint(1, 10) for _ in range(num_questions)]
    
    response = {
        "user_id": user_id,
        "question_ids": question_ids_selected,
        "answer_ids": answer_ids_selected,
        "complete_time": complete_time,
        "time_for_question": time_for_question,
    }
    responses.append(response)

# Insert responses into MongoDB
response_collection.insert_many(responses)

print("Data inserted successfully.")
