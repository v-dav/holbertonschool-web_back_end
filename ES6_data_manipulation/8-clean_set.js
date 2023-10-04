export default function cleanSet(set, startString) {
  let myString = '';
  const arr = Array.from(set);
  for (let i = 0; i < arr.length; i += 1) {
    if (typeof startString === 'string' && startString !== '' && arr[i].startsWith(startString)) {
      myString += arr[i].slice(startString.length);
      if (i !== arr.length - 2) {
        myString += '-';
      }
    }
  }
  return myString;
}
