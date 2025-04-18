const express = require('express');
const router = express.Router();
const { getFullPizzaByItemId } = require('../controllers/fullPizzaController');

router.get('/:itemId', getFullPizzaByItemId);

module.exports = router;
