from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["library_app"]
books = db["books"]

book = [{
    "title": "Python Basic",
    "author": "John Doe",
    "year": 2024,
    "tags": ["python", "programming"]
},
{
    "title": "MongoDB Basic",
    "author": "John Meo",
    "year": 2024,
    "tags": ["pymongo", "MongoClient"]
},
{
    "title": "Java Basic",
    "author": "John Seo",
    "year": 2024,
    "tags": ["javac", ".java"]
}]

query ={"author": "John Seo"}
result = books.insert_many(book)
for doc in books.find():
    print(doc)
    
result = books.find_one(query)
print(f"Got the book : {result}")

client.close()
