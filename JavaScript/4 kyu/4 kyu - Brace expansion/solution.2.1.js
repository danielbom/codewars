function combineWords(leftWords, rightWords) {
  const result = [];

  for (let leftWord of leftWords) {
    for (let rightWord of rightWords) {
      result.push(leftWord + rightWord);
    }
  }

  return result;
}

class BraceParser {
  /*
    expression     = component, component, ...
    component      = component_part component_part ...
    component_part = letters | (expression)
  */
  parse(expression) {
    this.expression = expression;
    this.nextCharIndex = 0;

    return this.parseExpression();
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
    if (!this.peek()) return null;

    let str = "";
    const specialChars = "{,}";
    while (!this.eof()) {
      const ch = this.readNextChar();
      if (!specialChars.includes(ch)) {
        str += ch;
      } else {
        this.unreadChar();
        break;
      }
    }

    return str;
  }

  unreadChar() {
    this.nextCharIndex--;
  }

  readNextChar() {
    return this.expression[this.nextCharIndex++];
  }

  peek() {
    return this.expression[this.nextCharIndex];
  }

  eof() {
    return this.nextCharIndex === this.expression.length;
  }
}

function expandBraces(str) {
  let result = str.split("{", 1);

  let start = 0;
  for (let i = start; i < str.length; i++) {
    if (str[i] === "{") {
      if (start !== 0 && start !== i) {
        result = combineWords(result, [str.slice(start, i)]);
      }

      let count = 1;
      let end = i + 1;
      while (count !== 0) {
        count += str[end] === "{";
        count -= str[end] === "}";
        end++;
      }

      const right = new BraceParser().parse(str.slice(i, end));

      result = combineWords(result, right);

      i = start = end;
    }
  }

  result = combineWords(result, [str.slice(start)]);
  return result;
}

module.exports = expandBraces;
