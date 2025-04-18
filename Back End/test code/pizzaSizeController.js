const PizzaSize = require('../models/PizzaSize');

exports.getAllSizes = async (req, res) => {
  try {
    const sizes = await PizzaSize.find();
    res.json(sizes);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

exports.getSizeById = async (req, res) => {
  try {
    const size = await PizzaSize.findOne({ SizeID: req.params.id });
    if (!size) return res.status(404).json({ message: 'Size not found' });
    res.json(size);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

