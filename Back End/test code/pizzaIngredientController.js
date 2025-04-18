const PizzaIngredient = require('../models/PizzaIngredient');


exports.getAllIngredients = async (req, res) => {
  try {
    const allPizzas = await PizzaIngredient.find(); // correct variable
    res.json(allPizzas); // respond with the correct variable
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};


exports.getIngredientsByItemID = async (req, res) => {
  try {
    const pizza = await PizzaIngredient.findOne({ ItemID: req.params.itemId });
    if (!pizza) {
      return res.status(404).json({ message: 'Pizza not found' });
    }
    res.json(pizza);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

