"""DAY 6–7 – MINI PROJECT: STUDENT MANAGER CLI

🎯 Goal: Combine all CRUD operations into a simple Python-based CLI tool.

Features to Implement

Add a student

Show all students

Search student by name

Update marks

Delete student by roll number"""


# print("=========STUDENT MANAGER CLI==========")

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["Student_Manager_DB"]
# students = db["students"]

# while True:
#     print("\n1. Add Student\n2. Show All\n3. Search\n4. Update\n5. Delete\n6. Exit")
#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         # call insert function
#         num = int(input("Enter the number of students you want to insert: "))
#         for i in range(0, num):
#             name = input(f"Enter the name of the student[{i}]: ")
#             roll = int(input(f"Enter the roll of the student[{i}]: "))
#             marks = int(input(f"Enter the marks of the student[{i}]: "))
            
#             student = {
#                 "name": name,
#                 "roll": roll,
#                 "marks": marks
#             }

#             result = students.insert_one(student)
#             print(f"Student inserted : {result.inserted_id}")
        
#     elif choice == 2:
#         # call read function
#         for docs in students.find():
#             print(docs)
#     elif choice == 3:
#         # find by name
#         name = input("Please enter name to search: ")
#         for docs in students.find({"name" : name}):
#             print(docs)
#     elif choice == 4:
#         # update marks
#         name = input("Enter the name of the student: ")
#         marks = int(input("Enter the marks: "))
#         students.update_one({"name": name}, {"$set": {"marks": marks}})
#         print(f"Students marks updated: {name} : {marks}")
        
#     elif choice == 5:
#         # delete by roll
#         roll = int(input("Enter the roll of the student: "))
#         students.delete_one({"roll": roll})
#         print("Student deleted successfully!..")
        
#     elif choice == 6:
#         break
    
#     else:
#         print("Invalid choice!..")

print("========= STUDENT MANAGER CLI ==========")

from pymongo import MongoClient, errors

try:
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Student_Manager_DB"]
    students = db["students"]
except errors.ConnectionFailure:
    print("Failed to connect to MongoDB. Please ensure MongoDB is running.")
    exit()

while True:
    print("\n1. Add Student\n2. Show All\n3. Search\n4. Update\n5. Delete\n6. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1–6.")
        continue

    if choice == 1:
        # Add student(s)
        num = int(input("Enter the number of students you want to insert: "))
        for i in range(num):
            name = input(f"Enter the name of student[{i + 1}]: ")
            roll = int(input(f"Enter the roll number of student[{i + 1}]: "))
            marks = int(input(f"Enter the marks of student[{i + 1}]: "))

            # Check duplicate roll
            if students.find_one({"roll": roll}):
                print(f"Student with roll {roll} already exists. Skipping...")
                continue

            student = {"name": name, "roll": roll, "marks": marks}
            result = students.insert_one(student)
            print(f"Student inserted: {result.inserted_id}")

    elif choice == 2:
        # Show all
        print("\n-- All Students --")
        for doc in students.find():
            print(f"Name: {doc['name']}, Roll: {doc['roll']}, Marks: {doc['marks']}")

    elif choice == 3:
        # Search by name
        name = input("Enter name to search: ")
        found = False
        for doc in students.find({"name": name}):
            print(f"Name: {doc['name']}, Roll: {doc['roll']}, Marks: {doc['marks']}")
            found = True
        if not found:
            print("No student found with that name.")

    elif choice == 4:
        # Update marks
        name = input("Enter the name of the student: ")
        marks = int(input("Enter the new marks: "))
        result = students.update_one({"name": name}, {"$set": {"marks": marks}})

        if result.modified_count > 0:
            print(f"Updated marks for {name}.")
        else:
            print("Student not found or marks unchanged.")

    elif choice == 5:
        # Delete by roll
        roll = int(input("Enter the roll number of the student: "))
        result = students.delete_one({"roll": roll})

        if result.deleted_count > 0:
            print("Student deleted successfully!")
        else:
            print("No student found with that roll number.")

    elif choice == 6:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1–6.")

