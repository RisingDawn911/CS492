const express = require('express');
const router = express.Router();
const cartController = require('../../controllers/customer/cartController');
const verifyCustomer = require('../../middleware/verifyCustomer');

router.post('/', verifyCustomer, cartController.addToCart);
router.get('/:userId', verifyCustomer, cartController.getCartByUser);
router.delete('/:itemId', verifyCustomer, cartController.removeItemFromCart); // ✅ FIXED LINE

module.exports = router;

