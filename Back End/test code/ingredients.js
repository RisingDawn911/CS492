const express = require('express');
const router = express.Router();
const {
   getAllIngredients,
   getIngredientsByItemID
}  = require('../controllers/pizzaIngredientController');

router.get('/', getAllIngredients);
router.get('/:itemId', getIngredientsByItemID);

module.exports = router;