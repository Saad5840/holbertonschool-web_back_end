// full_server/utils.js
import { promises as fs } from 'fs';

export default async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');

    const lines = data
      .split('\n')
      .filter((line) => line.trim() !== '');

    // Handle empty or header-only CSV: return empty mapping
    if (lines.length <= 1) {
      return {};
    }

    // Remove header
    lines.shift();

    // Build mapping: { field: [firstnames...] }
    const fields = {};
    for (const line of lines) {
      const parts = line.split(',');
      if (parts.length < 4) continue;

      const firstname = parts[0].trim();
      const field = parts[3].trim();
      if (!firstname || !field) continue;

      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
    }

    return fields;
  } catch (err) {
    // Propagate read error (controller will map to proper status)
    throw err;
  }
}
