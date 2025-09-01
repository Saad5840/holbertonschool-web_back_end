#!/usr/bin/node

const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (e) {
    throw new Error('Cannot load the database');
  }

  const lines = data
    .split('\n')
    .filter((line) => line.trim() !== '');

  // No students if only header (or nothing) — do NOT throw, just print totals as 0s if applicable
  if (lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  // Remove header row
  const header = lines.shift(); // eslint-disable-line no-unused-vars

  const fields = {}; // { field: [firstnames...] }
  let total = 0;

  for (const line of lines) {
    const parts = line.split(',');
    if (parts.length < 4) continue; // skip malformed/empty
    const firstname = parts[0].trim();
    const field = parts[3].trim();
    if (!firstname || !field) continue;

    if (!fields[field]) fields[field] = [];
    fields[field].push(firstname);
    total += 1;
  }

  console.log(`Number of students: ${total}`);

  // Keep insertion order of fields as they first appear in the CSV
  for (const field of Object.keys(fields)) {
    const list = fields[field];
    console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
  }
}

module.exports = countStudents;
