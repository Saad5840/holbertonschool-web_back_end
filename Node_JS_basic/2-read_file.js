#!/usr/bin/node

const fs = require('fs');

function countStudents(path) {
  try {
    // Read file content synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split lines and remove empty ones
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove header
    lines.shift();

    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    // Track students and fields
    const students = {};
    const allFirstNames = [];

    for (const line of lines) {
      const parts = line.split(',');
      if (parts.length === 4) {
        const firstname = parts[0].trim();
        const field = parts[3].trim();

        allFirstNames.push(firstname);

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }
    }

    // Print total
    console.log(`Number of students: ${allFirstNames.length}`);

    // Print per field
    for (const field of Object.keys(students)) {
      console.log(
        `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
