const CartItem = require('../models/CartItem');


exports.addToCart = async (req, res) => {
  try {
    const { userId, pizza } = req.body;

    const cartItem = new CartItem({ userId, pizza });
    await cartItem.save();

    res.status(201).json({
      message: 'Pizza added to cart',
      cartItem: {
        id: cartItem._id,
        userId: cartItem.userId,
        pizza: cartItem.pizza,
        timestamp: cartItem.timestamp
      }
    });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

exports.getCartByUser = async (req, res) => {
  try {
    const { userId } = req.params;
    const cartItems = await CartItem.find({ userId });

    const formattedCart = cartItems.map(item => ({
      id: item._id,
      userId: item.userId,
      pizza: item.pizza,
      timestamp: item.timestamp
    }));

    res.json({
      userId,
      cart: formattedCart
    });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

exports.clearCart = async (req, res) => {
  try {
    const { userId } = req.params;
    await CartItem.deleteMany({ userId });
    res.json({ message: 'Cart cleared' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

exports.deleteCartItem = async (req, res) => {
    try {
      const { itemId } = req.params;
      const deletedItem = await CartItem.findByIdAndDelete(itemId);
  
      if (!deletedItem) {
        return res.status(404).json({ message: 'Cart item not found' });
      }
  
      res.json({
        message: 'Cart item deleted',
        deletedItem
      });
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  };