export default function iterateThroughObject(reportWithIterator) {
  let employeesString = '';
  const employeesArray = Array.from(reportWithIterator);
  const lastIndex = employeesArray.length - 1;

  for (const [index, employee] of employeesArray.entries()) {
    employeesString += employee;
    if (index !== lastIndex) {
      employeesString += ' | ';
    }
  }
  return employeesString;
}
