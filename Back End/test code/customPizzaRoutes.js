const express = require('express');
const router = express.Router();
const { calculateCustomPizzaPrice } = require('../controllers/customPizzaController');

router.post('/price', calculateCustomPizzaPrice);

module.exports = router;
