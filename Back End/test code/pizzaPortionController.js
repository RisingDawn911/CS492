const PizzaPortion = require('../models/PizzaPortion');

// GET all portions
exports.getAllPortions = async (req, res) => {
  try {
    const portions = await PizzaPortion.find();
    res.json(portions);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

// GET portion by ID
exports.getPortionById = async (req, res) => {
  try {
    const portion = await PizzaPortion.findOne({ PortionID: req.params.id });
    if (!portion) return res.status(404).json({ message: 'Portion not found' });
    res.json(portion);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};
