export default function createIteratorObject(report) {
  // iterable object...
  const myIterable = {
    // that has a special method...
    [Symbol.iterator]() {
      let departmentIndex = 0;
      let employeeIndex = 0;
      // that returns a special object calle d iterator...
      return {
        // that has a special method witch returns the next element in the iteration sequence
        next() {
          const departmentNames = Object.keys(report.allEmployees);
          const departmentName = departmentNames[departmentIndex];
          const department = report.allEmployees[departmentName];
          if (departmentIndex < Object.keys(report.allEmployees).length) {
            if (employeeIndex < department.length) {
              const employee = department[employeeIndex];
              employeeIndex++;
              return {
                value: employee,
                done: false,
              };
            }
            // go to next department
            employeeIndex = 0;
            departmentIndex++;
            return this.next();
          }
          return {
            value: undefined,
            done: true,
          };
        },
      };
    },
  };
  return myIterable;
}
