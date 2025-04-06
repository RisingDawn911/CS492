from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrderingAdmin"]
collection = db["WebsiteChangeLog"]

# Added an index on the "LogID" field to facilitate faster data queries.
collection.create_index(["LogID"])

# Added an compound index on the "User" and "ActionDate" fields to facilitate faster data queries.
collection.create_index(["User", "ActionDate"])

# This creates the frame for inserting my array of documents into MongoDB
ChangeLog = [
    {
        "LogID": "Test1",
        "User": "John Malkovich",
        "Action": "Performed Test on Logs.",
        "ActionDate": "2025/04/05",
        "ActionStatus": "Successful",
    }
]

# This inserts the data into the collection.
result = collection.insert_many(ChangeLog)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()