const express = require('express');
const router = express.Router();

const {
  getAllSizes,
  getSizeById
} = require('../controllers/PizzaSizeController'); 

router.get('/', getAllSizes);
router.get('/:id', getSizeById);

module.exports = router;
