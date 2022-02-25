// https://www.codewars.com/kata/597f11f61fe82a80c200002c/train/javascript
// My solution 1
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

// My solution 2
// Based on
// https://stackoverflow.com/questions/28526013/bash-brace-expansion-algorithm

function combineWords(leftWords, rightWords) {
  const result = [];

  for (const leftWord of leftWords) {
    for (const rightWord of rightWords) {
      result.push(leftWord + rightWord);
    }
  }

  return result;
}

class BraceParser {
  parse(str) {
    this.str = str;
    this.index = 0;

    return this.startParse();
  }

  startParse() {
    let result = [""];

    while (!this.eof()) {
      const letters = this.readOuterLetters();

      result = combineWords(result, [letters]);

      if (this.peek() === "{") {
        this.readNextChar();
        const rightItems = this.parseExpression();
        result = combineWords(result, rightItems);
        this.readNextChar();
      }
    }

    return result;
  }

  readOuterLetters() {
    let str = "";

    while (!this.eof()) {
      const ch = this.readNextChar();

      if (ch === "{") {
        this.unreadChar();
        break;
      } else if (ch === "}") {
        break;
      } else {
        str += ch;
      }
    }

    return str;
  }

  parseExpression() {
    let result = [];

    while (!this.eof()) {
      const items = this.parseComponent();
      result = result.concat(items);

      if (this.peek() === ",") {
        this.readNextChar();
      } else {
        break;
      }
    }

    return result;
  }

  parseComponent() {
    let leftItems = [""];

    while (!this.eof()) {
      let rightItems = this.parseComponentPart();

      if (rightItems === null) {
        break;
      }

      leftItems = combineWords(leftItems, rightItems);
    }

    return leftItems;
  }

  parseComponentPart() {
    const nextChar = this.peek();

    if (nextChar === "{") {
      this.readNextChar();

      let items = this.parseExpression();

      this.readNextChar();

      return items;
    } else if (nextChar) {
      let letters = this.readLetters();
      if (letters === null) return null;
      if (letters.length === 0) return null;
      return [letters];
    } else {
      return null;
    }
  }

  readLetters() {
    let str = "";

    while (!this.eof()) {
      const ch = this.readNextChar();
      if ("{,}".includes(ch)) {
        this.unreadChar();
        break;
      } else {
        str += ch;
      }
    }

    return str;
  }

  unreadChar() {
    this.index--;
  }

  readNextChar() {
    const ch = this.peek();
    this.index++;
    return ch;
  }

  peek() {
    return this.str[this.index];
  }

  eof() {
    return this.str.length <= this.index;
  }
}

function expandBraces(str) {
  return new BraceParser().parse(str);
}

// My solution 3
function tokenize(str) {
  const n = str.length;
  const rootToken = {
    start: 0,
    end: n,
    children: [],
    elems: [],
    parent: null,
    type: "ROOT",
    depth: 0
  };
  const tokens = [rootToken];

  function braceTraverse(start, parent) {
    const braceToken = {
      start,
      end: -1,
      children: [],
      elems: [],
      parent,
      type: "BRACE",
      depth: parent.depth + 1
    }
    parent.children.push(braceToken);
    tokens.push(braceToken);
    
    let lastI = start + 1;
    let i = lastI;
    for (; i < n; i++) {
      if (str[i] === '}') {
        break;
      } else if (str[i] === '{') {
        i = braceTraverse(i, braceToken);
      } else if (str[i] === ',') {
        braceToken.elems.push({
          start: lastI,
          end: i,
          type: "COMMA",
          parent: braceToken,
          depth: parent.depth + 1
        });
        lastI = i + 1;
      }
    }
    braceToken.end = i + 1;
    braceToken.elems.push({
      start: lastI,
      end: i,
      type: "COMMA",
      parent: braceToken,
      depth: parent.depth + 1
    });
    return i;
  }
  
  for (let i = 0; i < n; i++) {
    if (str[i] === '{') {
      i = braceTraverse(i, rootToken);
    }
  }
  return tokens[0];
}

function expand1(str) {
  const rootToken = tokenize(str);
  let result = [str];
  let completed = true;

  function extract(token) {
    return str.slice(token.start, token.end);
  }
  
  rootToken.children.reverse().map(c => {
    if (c.children.length > 0) completed = false;

    result = result.reduce((arr, s) => {
      c.elems.forEach(e => {
        arr.push(s.slice(0, c.start) + extract(e) + s.slice(c.end));
      });
      return arr;
    }, []);
  });
  
  return { result, completed };
}

function expandBraces(str) {
  const it = expand1(str);

  if (!it.completed) {
    return it.result.reduce((arr, s) => {
      arr.push(...expandBraces(s));
      return arr;
    }, []);
  } else {
    return it.result;
  }
}

// ,,,
function expandBraces(str) {
  const count = c => c == '{' ? 1 : c == '}' ? -1 : 0
  let start = str.indexOf('{'), end = start + 1, ctr = 1      // Find first/next `{`   |  Counter used to count nested braces
  if (start<0) return [str]                                   // No braces? All done!
  while (ctr) ctr += count(str[end++])                        // Iterate thru `str` until find matching `}`
  
  return [...str.slice(start+1,end-1)]                        // Turn first brace grouping into array of chars
  .map(c => !(ctr += count(c)) && c==',' ? ';' : c )          // Mark commas at top level only (replace with `;`)
  .join('').split(';')                                        // Create array of choices
  .map(s => str.slice(0,start) + s + str.slice(end))          // Map back into orig str
  .reduce((all,some) => all.concat(expandBraces(some)), [])   // Recurse in case any more braces (nested or alone)
}
