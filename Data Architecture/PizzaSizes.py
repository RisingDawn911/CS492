from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrdering"]
collection = db["PizzaSizes"]

# This creates the frame for inserting my array of documents into MongoDB
pizzasize = [
    {
        "SizeID": "SZ1",
        "SizeName": "Small",
        "InchDiam": "12-Inch",
        "SizePriceAdd": 0.00
    },
    {
        "SizeID": "SZ2",
        "SizeName": "Medium",
        "InchDiam": "16-Inch",
        "SizePriceAdd": 4.00
    },
    {
        "SizeID": "SZ3",
        "SizeName": "Large",
        "InchDiam": "22-Inch",
        "SizePriceAdd": 10.00
    }
]

# This inserts the data into the collection.
result = collection.insert_many(pizzasize)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()