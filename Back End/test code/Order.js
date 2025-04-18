const mongoose = require('mongoose');

const OrderSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  pizzas: [
    {
      ItemID: String,
      SelectedIngredients: [
        {
          Name: String,
          Portion: String
        }
      ],
      SizeID: String,
      FinalPrice: Number
    }
  ],
  timestamp: { type: Date, default: Date.now }
}, {
  collection: 'Orders'
});

module.exports = mongoose.model('Order', OrderSchema);
