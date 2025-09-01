#!/usr/bin/node

const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (e) {
    throw new Error('Cannot load the database');
  }

  // Split and drop empty lines (including trailing blanks)
  const rows = content.split('\n').filter((line) => line.trim() !== '');
  if (rows.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  // Remove header
  rows.shift();

  const fields = {}; // { FIELD: [firstnames...] }
  let total = 0;

  for (const line of rows) {
    const parts = line.split(',');
    if (parts.length < 4) continue; // skip malformed
    const firstname = parts[0].trim();
    const field = parts[3].trim();
    if (!firstname || !field) continue;

    if (!fields[field]) fields[field] = [];
    fields[field].push(firstname);
    total += 1;
  }

  console.log(`Number of students: ${total}`);

  // Keep order of first appearance in the CSV
  for (const field of Object.keys(fields)) {
    const list = fields[field];
    console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
  }
}

module.exports = countStudents;
