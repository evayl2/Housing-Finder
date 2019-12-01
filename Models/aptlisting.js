const mongoose = require('mongoose');
const aptSchema = new mongoose.Schema({
  name: String,
  beds: Number,
  baths: Number,
  price: Number,
  location: Number
});
module.exports = mongoose.model('Apartment Listing', aptSchema);
