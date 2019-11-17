const mongoose = require('mongoose');
const UserSchema = new mongoose.Schema({
  username: String,
  password: String,
  major: String,
  numBeds: Number,
  groupNum: String,
  description: String
});
module.exports = mongoose.model('User', UserSchema);
