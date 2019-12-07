require('dotenv').config({ path: './variables.env' });

const connectToDatabase = require('./db');
const aptListing = require('../Desktop/Models/aptlisting');

'use strict';

module.exports.create = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  connectToDatabase()
  .then(() => {
    aptListing.create(JSON.parse(event.body))
      .then(apt => callback(null, {
        statusCode: 200,
        body: JSON.stringify(apt)
      }))
      .catch(err => callback(null, {
        statusCode: err.statusCode || 500,
        headers: { 'Content-Type': 'text/plain' },
        body: 'Could not create the apartment listing.'
      }));
  });
};
module.exports.getOne = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  connectToDatabase()
  .then(() => {
    aptListing.findById(event.pathParameters.id)
      .then(apt => callback(null, {
        statusCode: 200,
        body: JSON.stringify(apt)
      }))
      .catch(err => callback(null, {
        statusCode: err.statusCode || 500,
        headers: { 'Content-Type': 'text/plain' },
        body: 'Could not fetch the apartment listing.'
      }));
  });
};
module.exports.getAll = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  connectToDatabase()
  .then(() => {
    aptListing.find()
      .then(apt => callback(null, {
        statusCode: 200,
        body: JSON.stringify(apt)
      }))
      .catch(err => callback(null, {
        statusCode: err.statusCode || 500,
        headers: { 'Content-Type': 'text/plain' },
        body: 'Could not fetch the apartment listing.'
      }))
  });
};
module.exports.update = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  connectToDatabase()
  .then(() => {
    aptListing.findByIdAndUpdate(event.pathParameters.id, JSON.parse(event.body), { new: true })
      .then(apt => callback(null, {
        statusCode: 200,
        body: JSON.stringify(apt)
      }))
      .catch(err => callback(null, {
        statusCode: err.statusCode || 500,
        headers: { 'Content-Type': 'text/plain' },
        body: 'Could not fetch the apartment listing.'
      }));
  });
};

module.exports.delete = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  connectToDatabase()
  .then(() => {
    aptListing.findByIdAndRemove(event.pathParameters.id)
      .then(apt => callback(null, {
        statusCode: 200,
        body: JSON.stringify({ message: 'Removed apartment listing with id: ' + apt._id, apt: apt })
      }))
      .catch(err => callback(null, {
        statusCode: err.statusCode || 500,
        headers: { 'Content-Type': 'text/plain' },
        body: 'Could not fetch the apartment listing.'
      }));
  });
};

//Function to get apartments based on the applied filters such as price, # of bed/baths.
module.exports.getFiltered = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  connectToDatabase()


};
