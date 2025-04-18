const Order = require('../../models/Order');
const Cart = require('../../models/Cart'); // 💡 Needed for cart-to-order automation

// POST /api/orders
exports.placeOrder = async (req, res) => {
  try {
    const { userId, items, totalPrice } = req.body;

    const newOrder = new Order({
      userId,
      items,
      totalPrice
    });

    await newOrder.save();

    res.status(201).json({ message: 'Order placed successfully!', order: newOrder });
  } catch (err) {
    res.status(500).json({ message: 'Error placing order', error: err.message });
  }
};

// GET /api/orders/:userId
exports.getOrdersByUser = async (req, res) => {
  try {
    const userOrders = await Order.find({ userId: req.params.userId });
    if (userOrders.length === 0) {
      return res.status(404).json({ message: 'No orders found for this user.' });
    }
    res.status(200).json(userOrders);
  } catch (err) {
    res.status(500).json({ message: 'Error retrieving orders', error: err.message });
  }
};

// GET /api/orders/status/:orderId
exports.getOrderStatus = async (req, res) => {
  try {
    const order = await Order.findById(req.params.orderId);
    if (!order) {
      return res.status(404).json({ message: 'Order not found.' });
    }
    res.status(200).json({
      orderId: order._id,
      status: order.status
    });
  } catch (err) {
    res.status(500).json({ message: 'Error retrieving order status', error: err.message });
  }
};

// POST /api/orders/from-cart/:userId
exports.placeOrderFromCart = async (req, res) => {
  try {
    const userId = req.params.userId;

    // Step 1: Get cart items
    const cartItems = await Cart.find({ userId });
    if (cartItems.length === 0) {
      return res.status(400).json({ message: 'Cart is empty. Cannot place order.' });
    }

    // Step 2: Calculate total price
    const totalPrice = cartItems.reduce((total, item) => {
      return total + item.price * item.quantity;
    }, 0);

    // Step 3: Format items for order
    const items = cartItems.map(item => ({
      pizzaName: item.pizzaName,
      size: item.size,
      crust: item.crust,
      toppings: item.toppings,
      specialInstructions: item.specialInstructions,
      quantity: item.quantity,
      price: item.price
    }));

    // Step 4: Create order
    const newOrder = new Order({ userId, items, totalPrice });
    await newOrder.save();

    // Step 5: Clear cart
    await Cart.deleteMany({ userId });

    res.status(201).json({ message: 'Order placed from cart!', order: newOrder });
  } catch (err) {
    res.status(500).json({ message: 'Failed to place order from cart', error: err.message });
  }
};
