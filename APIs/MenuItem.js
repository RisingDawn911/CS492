const mongoose = require('mongoose');

const menuItemSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: String,
  sizeOptions: [String], // ["Small", "Medium", "Large"]
  crustOptions: [String], // ["Thin", "Stuffed"]
  price: { type: Number, required: true },
  available: { type: Boolean, default: true }
});

module.exports = mongoose.model('MenuItem', menuItemSchema);
