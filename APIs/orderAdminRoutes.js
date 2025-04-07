const express = require('express');
const router = express.Router();
const adminController = require('../../controllers/admin/orderAdminController');
const verifyAdmin = require('../../middleware/auth'); //

// GET: View all orders
router.get('/', verifyAdmin, adminController.getAllOrders);
router.put('/:orderId', verifyAdmin, adminController.updateOrderStatus);

module.exports = router;
