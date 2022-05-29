// https://www.codewars.com/kata/53005a7b26d12be55c000243/train/javascript
// My solution

class Interpreter {
  constructor() {
    this.vars = {};
    this.functions = {};
    this.precedences = {
      "*": 2,
      "/": 2,
      "%": 2,
      "+": 1,
      "-": 1,
      "=": 0,
    };
  }

  tokenize(program) {
    if (program === "") return [];

    const regex =
      /\s*([-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*/g;
    return program.split(regex).filter(function (s) {
      return !s.match(/^\s*$/);
    });
  }

  isNumber(token) {
    return token.match(/[0-9]*\.?[0-9]+/);
  }

  isOperator(token) {
    return token.match(/[-+*\/\%]/);
  }

  resolvePrecedence(node) {
    if (node.lhs.type === "op") {
      const p1 = this.precedences[node.value];
      const p2 = this.precedences[node.lhs.value];
      if (p1 > p2) {
        const rhs = node.lhs;
        node.lhs = rhs.rhs;
        rhs.rhs = node;
        return rhs;
      } else {
        return node;
      }
    }
    return node;
  }

  eval(node) {
    if (node.type === "num") return node.value;
    if (node.type === "op") {
      node = this.resolvePrecedence(node);

      const lhs = this.eval(node.lhs);
      const rhs = this.eval(node.rhs);
      if (node.value === "+") return lhs + rhs;
      if (node.value === "-") return lhs - rhs;
      if (node.value === "*") return lhs * rhs;
      if (node.value === "/") return lhs / rhs;
      if (node.value === "%") return lhs % rhs;
    }
    if (node.type === "assign") {
      const value = this.eval(node.expr);
      this.vars[node.name.value] = value;
      return value;
    }
    if (node.type === "var") {
      if (node.value in this.vars) {
        return this.vars[node.value];
      }
    }
    if (node.type === "paren") {
      return this.eval(node.expr);
    }
    console.error(node);
    throw new Error("(eval) Invalid node: " + node.type);
  }

  input(expr) {
    const tokens = this.tokenize(expr).map((token) => {
      if (this.isNumber(token)) {
        return { type: "num", value: Number(token) };
      } else if (this.isOperator(token)) {
        return { type: "op", value: token };
      } else if (token === "=") {
        return { type: "assign", value: token };
      } else if (token === "(") {
        return { type: "lparen", value: token };
      } else if (token === ")") {
        return { type: "rparen", value: token };
      } else {
        return { type: "var", value: token };
      }
    });

    let stackParen = [];
    let assign = null;
    let tree = null;
    for (let i = 0; i < tokens.length; i++) {
      if (tokens[i].type === "lparen") {
        if (tree !== null) {
          if (tree.type === "op") {
            stackParen.push(tree);
            tree = null;
            continue;
          }
        } else {
          stackParen.push(tree);
          continue;
        }
      } else if (tokens[i].type === "rparen") {
        if (stackParen.length > 0) {
          const previous = stackParen.pop();
          if (previous !== null) {
            previous.rhs = { type: "paren", expr: tree };
            tree = previous;
          } else {
            tree = { type: "paren", expr: tree };
          }
          continue;
        }
      } else if (tokens[i].type === "assign") {
        if (i === 1) {
          if (tree.type === "var") {
            tokens[i].name = tree;
            tree = tokens[i];
            continue;
          }
        }
      } else if (tokens[i].type === "num") {
        if (tree === null) {
          tree = tokens[i];
          continue;
        } else if (tree.type === "op") {
          tree.rhs = tokens[i];
          continue;
        } else if (tree.type === "assign") {
          assign = tree;
          tree = tokens[i];
          continue;
        }
      } else if (tokens[i].type === "op") {
        if (tree !== null) {
          if (tree.type === "num") {
            tokens[i].lhs = tree;
            tree = tokens[i];
            continue;
          } else if (tree.type === "var") {
            tokens[i].lhs = tree;
            tree = tokens[i];
            continue;
          } else if (tree.type === "paren") {
            tokens[i].lhs = tree;
            tree = tokens[i];
            continue;
          } else if (tree.type === "op") {
            if (tree.rhs) {
              tokens[i].lhs = tree;
              tree = tokens[i];
              continue;
            }
          }
        }
      } else if (tokens[i].type === "var") {
        if (tree === null) {
          tree = tokens[i];
          continue;
        } else if (tokens[i].value in this.vars) {
          tokens[i].value = this.vars[tokens[i].value];
          tokens[i].type = "num";
          i--;
          continue;
        }
      }
      console.error(tokens);
      throw new Error("(ast) Invalid token: " + i + " '" + expr + "'");
    }

    if (stackParen.length !== 0) {
      throw new Error("(ast) Invalid paren construction: '" + expr + "'");
    }

    if (assign != null) {
      assign.expr = tree;
      tree = assign;
    }

    return tree === null ? "" : this.eval(tree);
  }
}
