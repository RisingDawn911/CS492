const mongoose = require('mongoose');

const IngredientSchema = new mongoose.Schema({
  Name: String,
  Portion: String,
});

const PizzaIngredientSchema = new mongoose.Schema({
  ItemID: String,
  ItemName: String,
  Ingredients: [IngredientSchema],
}, {
  collection: 'PizzaIngredients' 
});

module.exports = mongoose.model('PizzaIngredient', PizzaIngredientSchema);
