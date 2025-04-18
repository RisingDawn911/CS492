const PizzaPrice = require('../models/PizzaPrice');
const PizzaPortion = require('../models/PizzaPortion');
const PizzaSize = require('../models/PizzaSize');
const PizzaIngredient = require('../models/PizzaIngredient');

exports.calculateCustomPizzaPrice = async (req, res) => {
  const { ItemID, SelectedIngredients, SizeID } = req.body;

  try {
    const priceData = await PizzaPrice.findOne({ ItemID });
    const sizeData = await PizzaSize.findOne({ SizeID });
    const portionData = await PizzaPortion.find();
    const defaultIngredientData = await PizzaIngredient.findOne({ ItemID });

    if (!priceData || !sizeData || !defaultIngredientData) {
      return res.status(404).json({ message: 'Item, size, or ingredients not found' });
    }

    const basePrice = priceData.ItemPrice;
    const sizeAdd = sizeData.SizePriceAdd;

    const defaultIngredients = defaultIngredientData.Ingredients;

    let ingredientAddTotal = 0;
    const includedIngredients = [];
    const extraIngredients = [];

    SelectedIngredients.forEach(selected => {
      const isDefault = defaultIngredients.find(def =>
        def.Name === selected.Name && def.Portion === selected.Portion
      );

      const portionObj = portionData.find(p => p.PortionName === selected.Portion);
      const priceAdd = portionObj ? portionObj.PriceAdd : 0;

      if (isDefault) {
        includedIngredients.push({
          Name: selected.Name,
          Portion: selected.Portion
        });
      } else {
        ingredientAddTotal += priceAdd;
        extraIngredients.push({
          Name: selected.Name,
          Portion: selected.Portion,
          PriceAdd: priceAdd
        });
      }
    });

    const finalPrice = parseFloat((basePrice + sizeAdd + ingredientAddTotal).toFixed(2));

    res.json({
      BasePrice: basePrice,
      SelectedSize: {
        SizeID: sizeData.SizeID,
        SizeName: sizeData.SizeName,
        InchDiam: sizeData.InchDiam,
        SizePriceAdd: sizeAdd
      },
      IncludedIngredients: includedIngredients,
      ExtraIngredients: extraIngredients,
      IngredientAddTotal: ingredientAddTotal,
      FinalPrice: finalPrice
    });

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

  
