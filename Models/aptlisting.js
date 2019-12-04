const mongoose = require('mongoose');
const aptSchema = new mongoose.Schema({
  name: String,
  beds: Number,
  baths: Number,
  price: Number,
  latitude: Number,
  longitude: Number,
  address: String,
});
module.exports = mongoose.model('Apartment Listing', aptSchema);
