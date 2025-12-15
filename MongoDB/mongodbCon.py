from pymongo import MongoClient

# 1️⃣ Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["skillbarter"]
collection = db["users"]

# Clear the collection for clean testing (optional)
collection.delete_many({})

# 2️⃣ INSERT Operations
print("=== INSERTING DATA ===")
user1 = {"name": "Alice", "skill": "Python", "location": "Delhi"}
user2 = {"name": "Bob", "skill": "Java", "location": "Mumbai"}
user3 = {"name": "Eve", "skill": "Gardening", "location": "Kolkata"}

# Insert One
collection.insert_one(user1)

# Insert Many
collection.insert_many([user2, user3])

# 3️⃣ READ Operations
print("\n=== ALL USERS ===")
for user in collection.find():
    print(user)

print("\n=== FIND ONE USER (Alice) ===")
user = collection.find_one({"name": "Alice"})
print(user)

print("\n=== USERS WITH SKILL = 'Python' ===")
for user in collection.find({"skill": "Python"}):
    print(user)

# 4️⃣ UPDATE Operations
print("\n=== UPDATING ALICE'S LOCATION TO 'Bangalore' ===")
collection.update_one(
    {"name": "Alice"},
    {"$set": {"location": "Bangalore"}}
)

print("\n=== ADDING 'available: True' TO ALL PYTHON USERS ===")
collection.update_many(
    {"skill": "Python"},
    {"$set": {"available": True}}
)

# 5️⃣ DELETE Operations
print("\n=== DELETING USER WHERE NAME = 'Eve' ===")
collection.delete_one({"name": "Eve"})

# 6️⃣ OTHER USEFUL COMMANDS
print("\n=== USERS SORTED BY NAME ===")
for user in collection.find().sort("name", 1):
    print(user)

print("\n=== USERS (ONLY NAME AND SKILL) ===")
for user in collection.find({}, {"name": 1, "skill": 1, "_id": 0}):
    print(user)

print("\n=== TOTAL USER COUNT ===")
print(collection.count_documents({}))

# 7️⃣ CREATE INDEX (Optional for performance)
collection.create_index("name")

# 🔚 End
print("\n=== DONE ===")
