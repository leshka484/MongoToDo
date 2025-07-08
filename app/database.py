import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client: MongoClient = MongoClient(os.environ["MONGO_URL"])
db = client[os.environ["DB_NAME"]]
note_collection = db["notes"]
    
def get_note_collection():
    return note_collection

