const CartItem = require('../models/CartItem');
const Order = require('../models/Order');

exports.placeOrder = async (req, res) => {
  const { userId } = req.body;

  try {
    const cartItems = await CartItem.find({ userId });

    if (!cartItems.length) {
      return res.status(400).json({ message: 'Cart is empty' });
    }

    const pizzas = cartItems.map(item => item.pizza);

    const newOrder = new Order({ userId, pizzas });
    await newOrder.save();

    await CartItem.deleteMany({ userId }); // Clear cart after order

    res.status(201).json({
      message: 'Order placed successfully',
      orderId: newOrder._id,
      pizzas: newOrder.pizzas,
      timestamp: newOrder.timestamp
    });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};
