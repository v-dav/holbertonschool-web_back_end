export default function iterateThroughObject(reportWithIterator) {
  let employeesString = '';
  const lastIndex = reportWithIterator.length - 1;

  for (const employee of reportWithIterator) {
    employeesString += employee;
    if (reportWithIterator.indexOf(employee) !== lastIndex) {
      employeesString += ' | ';
    }
  }
  return employeesString;
}
