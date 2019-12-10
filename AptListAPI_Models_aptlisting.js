const mongoose = require('mongoose');
const aptSchema = new mongoose.Schema({
  name: String,
  beds: Number,
  baths: Number,
  major: String,
  priceMax: Number,
  priceMIN: Number,
  latitude: Number, 
  longitude: Number, 
  address: String,
  propertyGroup: String,
});
module.exports = mongoose.model('Apartment Listing', aptSchema);
