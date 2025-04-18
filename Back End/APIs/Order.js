const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  items: [
    {
      pizzaName: String,
      size: String,
      crust: String,
      toppings: [String],
      specialInstructions: String,
      quantity: Number,
      price: Number
    }
  ],
  totalPrice: { type: Number, required: true },
  status: {
    type: String,
    enum: ['Pending', 'Preparing', 'Out for Delivery', 'Delivered'],
    default: 'Pending'
  }
}, { timestamps: true });

module.exports = mongoose.model('Order', orderSchema);
