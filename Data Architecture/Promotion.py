from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This creates the frame for inserting my array of documents into MongoDB
promotions = [
    {
        "PromotionID": "BOGO",
        "PromotionName": "Buy One Get One",
        "PromotionDescription": "Double the Deliciousness! Buy One Pizza, Get One Absolutely FREE!",
        "SystemAction": "SELECT TOP FLOOR(COUNT(MAX(ItemNumber) / 2)  Pizzas ORDER BY Itemprice SET ItemPrice = 0"
    },
    {
        "PromotionID": "LRG3TPN",
        "PromotionName": "Large 3 - Topping Pizza",
        "PromotionDescription": "Feast Like Royalty for Just $12.99! Get a Large 3-Topping Pizza!",
        "SystemAction": "SELECT [ItemID] WHERE [ItemID] Contains 1CP and IngredientCount >= 5 SET ItemPrice = $12.99 + ($1.99 * [IngredientCount]  - 5)"
    }
]

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")  # Replace with your MongoDB connection string if needed

# This sets the database and collection (Table) I created.
db = client["PizzaOrdering"]
collection = db["PizzaPromotionInformation"]

# This inserts the data into the collection.
result = collection.insert_many(promotions)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.")

# Closes the connection.
client.close()