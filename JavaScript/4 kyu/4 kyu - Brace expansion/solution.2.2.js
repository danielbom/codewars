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
  /*
    input          = outer_letters
    expression     = component, component, ...
    component      = component_part component_part ...
    component_part = letters | (expression)
  */

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

module.exports = expandBraces;
