from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["libraryDB"]
books = db["books"]

book = {
    "title": "Python Basic",
    "author": "John Doe",
    "year": 2024,
    "tags": ["python", "programming"]
}

result = books.insert_one(book)
print(f"Inserted ID: {result.inserted_id}")

# Retrieve the document
for doc in books.find():
    print(doc)