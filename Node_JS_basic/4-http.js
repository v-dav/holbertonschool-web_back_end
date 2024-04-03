const http = require('http');

const port = 1245;
const hostname = '127.0.0.1';

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.statusCode(200);
  res.end('Hello Holberton School!');
});

app.listen(port, hostname);
module.exports = app;
