const express = require('express');
const router = express.Router();
const {
  addToCart,
  getCartByUser,
  clearCart
} = require('../controllers/cartController');

router.post('/', addToCart);             // POST /api/cart
router.get('/:userId', getCartByUser);   // GET /api/cart/:userId
router.delete('/:userId', clearCart);    // DELETE /api/cart/:userId

const { deleteCartItem } = require('../controllers/cartController');

router.delete('/item/:itemId', deleteCartItem); // DELETE /api/cart/item/:itemId

module.exports = router;
