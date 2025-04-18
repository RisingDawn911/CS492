const MenuItem = require('../../models/MenuItem');

// GET all menu items
exports.getMenu = async (req, res) => {
  try {
    const items = await MenuItem.find();
    res.status(200).json(items);
  } catch (err) {
    res.status(500).json({ message: 'Error getting menu', error: err.message });
  }
};

// POST new menu item
exports.addMenuItem = async (req, res) => {
  try {
    const newItem = new MenuItem(req.body);
    await newItem.save();
    res.status(201).json({ message: 'Item added to menu', item: newItem });
  } catch (err) {
    res.status(400).json({ message: 'Error adding item', error: err.message });
  }
};

// PUT update menu item
exports.updateMenuItem = async (req, res) => {
  try {
    const updated = await MenuItem.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!updated) return res.status(404).json({ message: 'Item not found' });
    res.status(200).json({ message: 'Item updated', item: updated });
  } catch (err) {
    res.status(500).json({ message: 'Error updating item', error: err.message });
  }
};

// DELETE menu item
exports.deleteMenuItem = async (req, res) => {
  try {
    const deleted = await MenuItem.findByIdAndDelete(req.params.id);
    if (!deleted) return res.status(404).json({ message: 'Item not found' });
    res.status(200).json({ message: 'Item deleted', item: deleted });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting item', error: err.message });
  }
};
