const Cart = require('../../models/Cart');

// POST /api/cart
exports.addToCart = async (req, res) => {
  try {
    const newItem = new Cart(req.body);
    await newItem.save();
    res.status(201).json({ message: 'Item added to cart!', data: newItem });
  } catch (err) {
    res.status(400).json({ message: 'Error adding to cart', error: err.message });
  }
};

// GET /api/cart/:userId
exports.getCartByUser = async (req, res) => {
  try {
    const items = await Cart.find({ userId: req.params.userId });
    res.status(200).json(items);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching cart', error: err.message });
  }
};


exports.removeItemFromCart = async (req, res) => {
  try {
    const item = await Cart.findByIdAndDelete(req.params.itemId);
    if (!item) return res.status(404).json({ message: 'Item not found' });
    res.status(200).json({ message: 'Item removed from cart' });
  } catch (err) {
    res.status(500).json({ message: 'Error removing item', error: err.message });
  }
};