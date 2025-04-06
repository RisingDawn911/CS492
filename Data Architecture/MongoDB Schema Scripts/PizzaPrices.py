from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrderingMenu"]
collection = db["PizzaPrices"]

# Added an index on the "ItemID" field to facilitate faster data queries.
collection.create_index(["ItemID"])

# This creates the frame for inserting my array of documents into MongoDB
MenuPrices = [
  {
    "ItemID": "1CP",
    "ItemName": "Cheese Pizza",
    "ItemPrice": 8.99,
    "DefaultIngredientCount": 2
  },
  {
    "ItemID": "1CP1",
    "ItemName": "1-Topping Pizza",
    "ItemPrice": 9.99,
    "DefaultIngredientCount": 3
  },
  {
    "ItemID": "1CP2",
    "ItemName": "2-Topping Pizza",
    "ItemPrice": 10.99,
    "DefaultIngredientCount": 4
  },
  {
    "ItemID": "2ML",
    "ItemName": "Meat Lovers",
    "ItemPrice": 14.99,
    "DefaultIngredientCount": 6
  },
  {
    "ItemID": "3HW",
    "ItemName": "Hawaiian",
    "ItemPrice": 12.99,
    "DefaultIngredientCount": 4
  },
  {
    "ItemID": "4BBQC",
    "ItemName": "BBQ Chicken",
    "ItemPrice": 13.99,
    "DefaultIngredientCount": 4
  },
  {
    "ItemID": "5BUFF",
    "ItemName": "Buffalo Chicken",
    "ItemPrice": 13.99,
    "DefaultIngredientCount": 4
  },
  {
    "ItemID": "6VEG",
    "ItemName": "Veggie",
    "ItemPrice": 11.99,
    "DefaultIngredientCount": 6
  },
  {
    "ItemID": "7DLX",
    "ItemName": "Deluxe",
    "ItemPrice": 14.99,
    "DefaultIngredientCount": 7
  }
]

# This inserts the data into the collection.
result = collection.insert_many(MenuPrices)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()



