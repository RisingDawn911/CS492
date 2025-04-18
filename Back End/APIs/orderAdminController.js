const Order = require('../../models/Order');

// GET /api/admin/orders
exports.getAllOrders = async (req, res) => {
  try {
    const orders = await Order.find().sort({ createdAt: -1 });
    res.status(200).json(orders);
  } catch (err) {
    res.status(500).json({ message: 'Error retrieving orders', error: err.message });
  }
};

// PUT /api/admin/orders/:orderId
exports.updateOrderStatus = async (req, res) => {
  try {
    const { status } = req.body;
    const order = await Order.findByIdAndUpdate(
      req.params.orderId,
      { status },
      { new: true }
    );

    if (!order) {
      return res.status(404).json({ message: 'Order not found.' });
    }

    res.status(200).json({ message: 'Order status updated.', order });
  } catch (err) {
    res.status(500).json({ message: 'Error updating order', error: err.message });
  }
};
