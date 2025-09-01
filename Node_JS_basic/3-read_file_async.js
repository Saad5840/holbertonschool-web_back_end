#!/usr/bin/node

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
        console.log('Number of students: 0');
        resolve();
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

      console.log(`Number of students: ${total}`);
      for (const field of Object.keys(fields)) {
        const list = fields[field];
        console.log(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
