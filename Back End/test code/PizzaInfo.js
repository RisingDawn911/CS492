const mongoose = require('mongoose');

const pizzaSchema = new mongoose.Schema({
  ItemID: String,
  ItemName: String,
  Description: String    
});

module.exports = mongoose.model('PizzaInfo', pizzaSchema, 'PizzaInfo');