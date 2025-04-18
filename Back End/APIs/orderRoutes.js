const express = require('express');
const router = express.Router();
const orderController = require('../../controllers/customer/orderController');
const verifyCustomer = require('../../middleware/verifyCustomer');

router.post('/', verifyCustomer, orderController.placeOrder);
router.get('/:userId', verifyCustomer, orderController.getOrdersByUser);
router.get('/status/:orderId', verifyCustomer, orderController.getOrderStatus);
router.post('/from-cart/:userId', verifyCustomer, orderController.placeOrderFromCart);

module.exports = router;
