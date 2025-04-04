import pymongo

# 1. Prepare your data
pizzas = [
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

# 2. Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://removedforsecurity.mongodb.net/?retryWrites=true&w=majority&appName=PizzaOrdering")  # Replace with your MongoDB connection string if needed

# 3. Access your database and collection
db = client["PizzaOrdering"]  # Replace "pizza_db" with your desired database name
collection = db["PizzaProductInformation"]  # Replace "pizzas" with your desired collection name

# 4. Insert the documents
result = collection.insert_many(pizzas)

print(f"Inserted {len(result.inserted_ids)} documents.")

# Close the connection
client.close()