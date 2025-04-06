from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrderingMenu"]
collection = db["PizzaPortions"]

# Added an index on the "PortionID" field to facilitate faster data queries.
collection.create_index(["PortionID"])

# This creates the frame for inserting my array of documents into MongoDB
pizzaportion = [
    {
        "PortionID": "PS0",
        "PortionName": "None",
        "PriceAdd": 0
    },
    {
        "PortionID": "PS1",
        "PortionName": "Light",
        "PriceAdd": 0
    },
    {
        "PortionID": "PS2",
        "PortionName": "Normal",
        "PriceAdd": 0
    },
    {
        "PortionID": "PS0",
        "PortionName": "Extra",
        "PriceAdd": 2
    }
]

# This inserts the data into the collection.
result = collection.insert_many(pizzaportion)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()