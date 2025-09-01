#!/usr/bin/node

const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      // Remove header
      lines.shift();

      const fields = {};
      let total = 0;

      for (const line of lines) {
        const parts = line.split(',');
        if (parts.length < 4) continue;

        const firstname = parts[0].trim();
        const field = parts[3].trim();

        if (!firstname || !field) continue;

        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
        total += 1;
      }

      let output = `Number of students: ${total}`;
      for (const field of Object.keys(fields)) {
        const list = fields[field];
        output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
      }

      resolve(output);
    });
  });
}

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(database)
      .then((output) => {
        res.end(output);
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
