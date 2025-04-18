const mongoose = require('mongoose');

const CartItemSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  pizza: {
    ItemID: String,
    SelectedIngredients: [
      {
        Name: String,
        Portion: String
      }
    ],
    SizeID: String,
    FinalPrice: Number
  },
  timestamp: { type: Date, default: Date.now }
}, {
  collection: 'CartItems'
});

module.exports = mongoose.model('CartItem', CartItemSchema);
