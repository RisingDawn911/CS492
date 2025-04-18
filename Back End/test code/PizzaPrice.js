const mongoose = require('mongoose');

const PizzaPriceSchema = new mongoose.Schema({
  ItemID: { type: String, required: true },
  ItemName: { type: String, required: true },
  ItemPrice: { type: Number, required: true },
  DefaultIngredientCount: { type: Number, required: true }
}, {
  collection: 'PizzaPrices' // <- match your actual MongoDB collection name
});

module.exports = mongoose.model('PizzaPrice', PizzaPriceSchema);
