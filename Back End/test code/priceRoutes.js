const express = require('express');
const router = express.Router();
const {
  getAllPrices,
  getPriceByItemID
} = require('../controllers/pizzaPriceController');

router.get('/', getAllPrices);
router.get('/:itemId', getPriceByItemID);

module.exports = router;
