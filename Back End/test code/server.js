require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('\u2714 Connected to PizzaOrderingMenu DB'))
  .catch(err => console.error('\u2716 MongoDB connection error:', err.message));

const pizzaRoutes = require('./routes/pizzaRoutes');
app.use('/api/pizzas', pizzaRoutes);

const ingredientRoutes = require('./routes/ingredients');
app.use('/api/ingredients', ingredientRoutes);

const portionRoutes = require('./routes/portionRoutes');
app.use('/api/portions', portionRoutes);

const priceRoutes = require('./routes/priceRoutes');
app.use('/api/prices', priceRoutes);

const sizeRoutes = require('./routes/sizeRoutes');
app.use('/api/sizes', sizeRoutes);

const fullPizzaRoutes = require('./routes/fullPizzaRoutes');
app.use('/api/fullPizza', fullPizzaRoutes);

const customPizzaRoutes = require('./routes/customPizzaRoutes');
app.use('/api/customPizza', customPizzaRoutes);

const cartRoutes = require('./routes/cartRoutes');
app.use('/api/cart', cartRoutes);

const orderRoutes = require('./routes/orderRoutes');
app.use('/api/orders', orderRoutes);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`[STARTED] Server running at http://localhost:${PORT}`));
