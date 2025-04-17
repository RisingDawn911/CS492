from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrderingMenu"]
collection = db["PizzaIngredients"]

# Added an index on the "ItemID" field to facilitate faster data queries.
collection.create_index(["ItemID"])

# This creates the frame for inserting my array of documents into MongoDB
PizzaIngredients = [
  {
    "ItemID": "1CP",
    "ItemName": "Cheese Pizza",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "None"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "1CP1",
    "ItemName": "1-Topping Pizza",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "None"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "1CP2",
    "ItemName": "2-Topping Pizza",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "None"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "2ML",
    "ItemName": "Meat Lovers",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "Normal"},
      { "Name": "Sausage", "Portion": "Normal" },
      { "Name": "Bacon", "Portion": "Normal"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "Normal" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "3HW",
    "ItemName": "Hawaiian",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "None"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "Normal" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "Normal" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "4BBQC",
    "ItemName": "BBQ Chicken",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "None" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "Normal" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "Normal"},
      { "Name": "Chicken", "Portion": "Normal" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "5BUFF",
    "ItemName": "Buffalo Chicken",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "None" },
      { "Name": "Buffalo Sauce", "Portion": "Normal" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "Normal"},
      { "Name": "Chicken", "Portion": "Normal" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "None" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "None" }
    ]
  },
  {
    "ItemID": "6VEG",
    "ItemName": "Veggie",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "None" },
      { "Name": "Sausage", "Portion": "None" },
      { "Name": "Bacon", "Portion": "None"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "Normal" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "Normal" },
      { "Name": "Red Onion", "Portion": "Normal" },
      { "Name": "Sweet Onion", "Portion": "Normal" }
    ]
  },
  {
    "ItemID": "7DLX",
    "ItemName": "Deluxe",
    "Ingredients": [
      { "Name": "Cheese Blend", "Portion": "Normal" },
      { "Name": "Red Sauce", "Portion": "Normal" },
      { "Name": "Buffalo Sauce", "Portion": "None" },
      { "Name": "BBQ Sauce", "Portion": "None" },
      { "Name": "Pepperoni", "Portion": "Normal" },
      { "Name": "Sausage", "Portion": "Normal" },
      { "Name": "Bacon", "Portion": "None"},
      { "Name": "Chicken", "Portion": "None" },
      { "Name": "Ham", "Portion": "None" },
      { "Name": "Green Pepper", "Portion": "Normal" },
      { "Name": "Pineapple", "Portion": "None" },
      { "Name": "Mushroom", "Portion": "Normal" },
      { "Name": "Red Onion", "Portion": "None" },
      { "Name": "Sweet Onion", "Portion": "Normal" }
    ]
  }
]

# This inserts the data into the collection.
result = collection.insert_many(PizzaIngredients)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()

