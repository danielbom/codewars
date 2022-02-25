// https://www.codewars.com/kata/52449b062fb80683ec000024/train/javascript
// My solution
function generateHashtag (str) {
  str = str.trim().replace(/\s+/, ' ');
  if (str.length == 0 || str.length >= 140) return false;
  return '#' + str.replace(/((^|\s+)\w)/g, (m) => m.trim().toUpperCase());
}

// ...
function generateHashtag (str) {
  return str.length > 140 || str === '' ? false :
    '#' + str.split(' ').map(capitalize).join('');
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// ...
function generateHashtag (str) {
  const hashtag = str.split(' ').reduce(function(tag, word) {
    return tag + word.charAt(0).toUpperCase() + word.substring(1);
  }, '#');
  
  return hashtag.length == 1 || hashtag.length > 140 ? false : hashtag;
}

// ...
function generateHashtag (str = "") {
  const hashtag = `#${str.trim().replace(/(?:\b|\s)(\w)/gi, (m, g) => g.toUpperCase())}`
  return !!str && hashtag.length <= 140 && hashtag
}
