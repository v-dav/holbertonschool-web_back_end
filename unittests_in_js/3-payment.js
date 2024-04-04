const { calculateNumber } = require('./utils')

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sumResult = calculateNumber('SUM', totalAmount, totalShipping)
  console.log(`Total is: ${sumResult}`)
}

module.exports = sendPaymentRequestToApi
