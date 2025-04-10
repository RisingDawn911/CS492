from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrderingAdmin"]
collection = db["AdminLogin"]

# Added an index on the "UserID" field to facilitate faster data queries.
collection.create_index(["UserID"])

# This creates the frame for inserting my array of documents into MongoDB
login = [
    {
        "UserID": "PL112",
        "Username": "PizzaLover112",
        "Password": "P!zZ@!sGr3@t",
        "Email": "admin@pizzastogo.com"
    }
]

# This inserts the data into the collection.
result = collection.insert_many(login)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()