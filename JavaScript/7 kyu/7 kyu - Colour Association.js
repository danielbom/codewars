// https://www.codewars.com/kata/56d6b7e43e8186c228000637/train/javascript
// My solution
function colourAssociation(array) {
  return array.map((pair) => {
    return { [pair[0]]: pair[1] };
  });
}
