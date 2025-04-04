#%%
import pandas as pd # Used to extract data from Excel Schema
from pymongo import MongoClient # Used to connect to the MongoDB
#%%
import pymongo

# 1. Prepare your data
MenuIngredients = [
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
      { "Name": "Green Pepper", "Portion": "None" },
      { "Name": "Pineapple", "Portion": "Normal" },
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

# 2. Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")  # Replace with your MongoDB connection string if needed

# 3. Access your database and collection
db = client["PizzaOrdering"]  # Replace "pizza_db" with your desired database name
collection = db["MenuIngredientInformation"]  # Replace "pizzas" with your desired collection name

# 4. Insert the documents
result = collection.insert_many(MenuIngredients)

print(f"Inserted {len(result.inserted_ids)} documents.")

# Close the connection
client.close()
#%%
