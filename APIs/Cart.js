const mongoose = require('mongoose');

const cartItemSchema = new mongoose.Schema({
  userId: {
    type: String,
    required: true
  },
  pizzaName: {
    type: String,
    required: true
  },
  size: {
    type: String,
    enum: ['Small', 'Medium', 'Large'],
    required: true
  },
  crust: {
    type: String,
    enum: ['Thin', 'Thick', 'Stuffed'],
    required: true
  },
  toppings: [String],
  specialInstructions: String,
  quantity: {
    type: Number,
    default: 1
  },
  price: {
    type: Number,
    required: true
  }
}, { timestamps: true });

const Cart = mongoose.model('Cart', cartItemSchema);
module.exports = Cart;
