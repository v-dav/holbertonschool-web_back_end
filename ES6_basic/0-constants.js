// a simple functions with constants

// a function with const
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

// a function
export function getLast() {
  return ' is okay';
}

// a function with let
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
