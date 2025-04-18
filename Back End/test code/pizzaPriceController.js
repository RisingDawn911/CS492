const PizzaPrice = require('../models/PizzaPrice');

// GET all prices
exports.getAllPrices = async (req, res) => {
  try {
    const prices = await PizzaPrice.find();
    res.json(prices);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

// GET price by ItemID
exports.getPriceByItemID = async (req, res) => {
  try {
    const price = await PizzaPrice.findOne({ ItemID: req.params.itemId });
    if (!price) return res.status(404).json({ message: 'Price not found' });
    res.json(price);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};
