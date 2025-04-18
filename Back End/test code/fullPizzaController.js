const PizzaIngredient = require('../models/PizzaIngredient');
const PizzaPrice = require('../models/PizzaPrice');
const PizzaSize = require('../models/PizzaSize');
const PizzaPortion = require('../models/PizzaPortion');

exports.getFullPizzaByItemId = async (req, res) => {
  const { itemId } = req.params;

  try {
    const ingredientData = await PizzaIngredient.findOne({ ItemID: itemId });
    const priceData = await PizzaPrice.findOne({ ItemID: itemId });
    const sizes = await PizzaSize.find();
    const portions = await PizzaPortion.find();

    if (!ingredientData || !priceData) {
      return res.status(404).json({ message: 'Pizza item not found' });
    }

    res.json({
      ItemID: itemId,
      ItemName: ingredientData.ItemName,
      Ingredients: ingredientData.Ingredients,
      Price: priceData.ItemPrice,
      DefaultIngredientCount: priceData.DefaultIngredientCount,
      AvailableSizes: sizes,
      AvailablePortions: portions
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
