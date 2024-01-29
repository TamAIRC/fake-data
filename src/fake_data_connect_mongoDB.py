import json
from pymongo import MongoClient
from faker import Faker
import random
import os

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DTU-test']  # Choose your database
users_collection = db['User']
user_info_collection = db['UserInformation']

# Create the directory if it doesn't exist
directory = 'data-fake/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate data using Faker
fake = Faker('vi_VN')

# Generate users
users = []
for _ in range(500000):
    user = {
        "age": round(random.uniform(15, 50), 0),
        "rank": round(random.uniform(1, 10), 0),
        "major": fake.word(),
        "previous_rank": round(random.uniform(1, 10), 0),
    }
    users.append(user)

# Insert users into MongoDB and retrieve their _id values
user_ids = []
for user in users:
    result = users_collection.insert_one(user)
    user_ids.append(result.inserted_id)

# Generate user information and reference user_id
users_information = []
for user_id in user_ids:
    user_information = {
        "user_id": user_id,  # Reference the user's _id
        "age": round(random.uniform(15, 50), 0),
        "major": fake.word(),
        "street_address": fake.sentence(),
        "phone_number": f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
    }
    users_information.append(user_information)

# Insert user information into MongoDB
user_info_collection.insert_many(users_information)

print("Data inserted successfully.")
