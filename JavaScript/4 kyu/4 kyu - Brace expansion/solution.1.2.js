function findCloseBrace(str, start) {
  let count = 0;
  let i = start;
  for (i = start; i < str.length; i++) {
    count += str[i] === "{";
    count -= str[i] === "}";
    if (count === 0) break;
  }
  return i;
}

function expand(str) {
  let words = [];
  let count = 0;
  let start = 0;
  for (let i = start; i < str.length; i++) {
    count += str[i] === "{";
    count -= str[i] === "}";
    if (str[i] === "," && count === 0) {
      words.push(str.slice(start, i));
      start = i + 1;
    }
  }
  words.push(str.slice(start));
  return [].concat(...words.map((w) => expandBraces(w)));
}

function expandBraces(str) {
  let words = str.split("{", 1);
  let start = 0;

  for (let i = start; i < str.length; i++) {
    if (str[i] === "{") {
      if (start !== 0 && start !== i) {
        const end = str.slice(start, i);
        words = words.map((w) => w + end);
      }
      const close = findCloseBrace(str, i);
      const expanded = expand(str.slice(i + 1, close));

      words = [].concat(...words.map((w1) => expanded.map((w2) => w1 + w2)));

      i = close;
      start = i + 1;
    }
  }

  if (start !== 0) {
    const end = str.slice(start);
    return words.map((w) => w + end);
  } else {
    return words;
  }
}

module.exports = expandBraces;
