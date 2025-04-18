const mongoose = require('mongoose');

const PizzaPortionSchema = new mongoose.Schema({
  PortionID: { type: String, required: true },
  PortionName: { type: String, required: true },
  PriceAdd: { type: Number, required: true }
}, {
  collection: 'PizzaPortions' // <- use exact collection name
});

module.exports = mongoose.model('PizzaPortion', PizzaPortionSchema);
