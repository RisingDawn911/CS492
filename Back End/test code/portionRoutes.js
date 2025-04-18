const express = require('express');
const router = express.Router();
const {
  getAllPortions,
  getPortionById
} = require('../controllers/pizzaPortionController');

router.get('/', getAllPortions);
router.get('/:id', getPortionById);

module.exports = router;
