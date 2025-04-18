const PizzaInfo = require('../models/PizzaInfo');


exports.getAllPizzas = async (req, res) => {
  try {
    const pizzas = await PizzaInfo.find();
    res.status(200).json(pizzas);
  } catch (err) {
    res.status(500).json({message: 'Failed to fecth pizzas', error: err.message });
  }
};