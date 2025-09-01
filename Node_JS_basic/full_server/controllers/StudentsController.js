// full_server/controllers/StudentsController.js
import readDatabase from '../utils.js';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const dbPath = process.argv[2];
    try {
      const fields = await readDatabase(dbPath);

      const header = 'This is the list of our students';
      // Sort field names case-insensitively
      const fieldNames = Object.keys(fields).sort((a, b) =>
        a.localeCompare(b, undefined, { sensitivity: 'base' })
      );

      const lines = [header];
      for (const field of fieldNames) {
        const list = fields[field] || [];
        lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }

      res.status(200).type('text/plain').send(lines.join('\n'));
    } catch (err) {
      res.status(500).type('text/plain').send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).type('text/plain').send('Major parameter must be CS or SWE');
      return;
    }

    const dbPath = process.argv[2];
    try {
      const fields = await readDatabase(dbPath);
      const list = fields[major] || [];
      res.status(200).type('text/plain').send(`List: ${list.join(', ')}`);
    } catch (err) {
      res.status(500).type('text/plain').send('Cannot load the database');
    }
  }
}
