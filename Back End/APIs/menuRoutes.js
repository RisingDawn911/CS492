const express = require('express');
const router = express.Router();
const menuController = require('../../controllers/admin/menuController');
const verifyAdmin = require('../../middleware/auth'); // 

// Admin Menu Routes
router.get('/', verifyAdmin, menuController.getMenu);
router.post('/', verifyAdmin, menuController.addMenuItem);
router.put('/:id', verifyAdmin, menuController.updateMenuItem);
router.delete('/:id', verifyAdmin, menuController.deleteMenuItem);

module.exports = router;
