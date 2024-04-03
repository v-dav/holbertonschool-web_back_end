const fs = require('fs');

function countStudents(path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) throw new Error('Cannot load the database');
    const dataArray = data.split('\n').slice(1).filter((line) => line !== '');
    console.log(`Number of students: ${dataArray.length}`);

    const namesbyField = {};
    dataArray.forEach((student) => {
      const studentArray = student.split(',');
      const name = studentArray[0];
      const field = studentArray[3];

      if (!namesbyField[field]) namesbyField[field] = [];
      namesbyField[field].push(name);
    });
    const fields = Object.keys(namesbyField);
    for (const field of fields) {
      const names = namesbyField[field];
      const count = names.length;
      console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    }
  });
}

countStudents('database.csv');
module.exports = countStudents;
