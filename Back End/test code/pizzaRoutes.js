const express = require('express');
const router = express.Router();
const controller = require('../controllers/pizzaInfoController');


router.get('/', controller.getAllPizzas);

module.exports = router;