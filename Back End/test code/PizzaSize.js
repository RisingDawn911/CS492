const mongoose = require('mongoose');

const PizzaSizeSchema = new mongoose.Schema({
  SizeID: { type: String, required: true },
  SizeName: { type: String, required: true },
  InchDiam: { type: String, required: true },
  SizePriceAdd: { type: Number, required: true }
}, {
  collection: 'PizzaSizes' // Match MongoDB collection name exactly
});

module.exports = mongoose.model('PizzaSize', PizzaSizeSchema);
