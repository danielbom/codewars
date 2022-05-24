// https://www.codewars.com/kata/56fcc393c5957c666900024d/train/javascript
// My solution
const ch = String.fromCharCode(11);
function code(text) {
  const n = Math.ceil(Math.sqrt(text.length));
  const m = n * n;
  const normalizedText = text + ch.repeat(m - text.length);

  const squaredStrings = [];
  for (let i = 0; i < m; i += n) {
    squaredStrings.push(normalizedText.slice(i, i + n));
  }

  const rotation = [];
  for (let i = 0; i < n; i++) {
    const result = [];
    for (let j = n - 1; j >= 0; j--) {
      result.push(squaredStrings[j][i]);
    }
    rotation.push(result.join(""));
  }
  return rotation.join("\n");
}

function decode(text) {
  const squaredStrings = text.split("\n");
  const n = Math.floor(Math.sqrt(text.length));

  const rotation = [];
  for (let i = n - 1; i >= 0; i--) {
    const result = [];
    for (let j = 0; j < n; j++) {
      result.push(squaredStrings[j][i]);
    }
    rotation.push(result.join(""));
  }

  return rotation.join("").replace(new RegExp(ch + "+$"), "");
}

// ...
function code(s) {
  let str = s.replace(/\n/g, ""),
    len = str.length,
    res = "";

  let n = Math.ceil(Math.sqrt(len)),
    m = n * (n - 1);

  for (var i = 0; i < n; i++) {
    res += "\n";

    for (var j = 0; j < n; j++) res += str[m + i - n * j] || "\v";
  }

  return res.slice(1);
}

function decode(s) {
  let res = code(code(code(s)));
  return res.replace(/(\n|\v)/g, "");
}
