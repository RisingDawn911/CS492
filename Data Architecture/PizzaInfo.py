from pymongo import MongoClient # Used to connect to the MongoDB
import pymongo

# This connects to my MongoDB server
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")

# This sets the database and collection (Table) I created.
db = client["PizzaOrdering"]  
collection = db["PizzaInfo"]  
# This creates the frame for inserting my array of documents into MongoDB

pizzainfo = [
    {
        "ItemID": "1CP",
        "ItemName": "Cheese Pizza",
        "Description": "A classic blend of melted Asiago, Mozzarella, and Cheddar cheeses, baked to golden perfection on our handmade crust with our signature red sauce. Simple, satisfying, and utterly delicious."
    },
    {
        "ItemID": "1CP1",
        "ItemName": "1-Topping Pizza",
        "Description": "Our handmade crust, topped with our signature red sauce and a generous layer of our three-cheese blend. Choose your favorite topping to create your perfect pizza!"
    },
    {
        "ItemID": "1CP2",
        "ItemName": "2-Topping Pizza",
        "Description": "Customize your culinary experience with our two-topping pizza. Starting with our handmade crust, signature red sauce, and a blend of Asiago, Mozzarella, and Cheddar cheeses, add your favorite duo of toppings."
    },
    {
        "ItemID": "2ML",
        "ItemName": "Meat Lovers",
        "Description": "A carnivore's dream! Our handmade crust loaded with our signature red sauce, a blend of Asiago, Mozzarella, and Cheddar cheeses, and piled high with savory pepperoni, Italian sausage, ham, and crispy bacon."
    },
    {
        "ItemID": "3HW",
        "ItemName": "Hawaiian",
        "Description": "A tropical twist on a classic. Our handmade crust, signature red sauce, and our three-cheese blend, topped with sweet pineapple chunks and savory ham."
    },
    {
        "ItemID": "4BBQC",
        "ItemName": "BBQ Chicken",
        "Description": "Tangy and delicious! Our handmade crust topped with BBQ sauce, a blend of Asiago, Mozzarella, and Cheddar cheeses, tender BBQ chicken, crispy bacon, and red onions."
    },
    {
        "ItemID": "5BUFF",
        "ItemName": "Buffalo Chicken",
        "Description": "Spice up your pizza night! Our handmade crust, buffalo sauce, a blend of Asiago, Mozzarella, and Cheddar cheeses, spicy buffalo chicken and crispy bacon."
    },
    {
        "ItemID": "6VEG",
        "ItemName": "Veggie",
        "Description": "A garden-fresh delight! Our handmade crust, signature red sauce, and our three-cheese blend, loaded with fresh mushrooms, crisp green peppers, and sweet onions."
    },
    {
        "ItemID": "7DLX",
        "ItemName": "Deluxe",
        "Description": "The ultimate combination. Our handmade crust, signature red sauce, a blend of Asiago, Mozzarella, and Cheddar cheeses, topped with pepperoni, Italian sausage, and mushrooms."
    }
]

# This inserts the data into the collection.
result = collection.insert_many(pizzainfo)

#Prints and output statement to show how many documents went into the database.
print(f"Inserted {len(result.inserted_ids)} documents.") 

# Closes the connection.
client.close()