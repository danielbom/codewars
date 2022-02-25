// https://www.codewars.com/kata/opposite-number/train/typescript
// My solution
export class Kata {
    static opposite(n: number) {
      return -n;
    }
}

// ...
export class Kata {
    static opposite(n: number) {
        // your code here
        const numberAsString = n.toString();
        const isNegative = /^-/.test(numberAsString);
        if(isNegative) {
            const absolute = numberAsString.replace(/^-/, '');
            return eval(absolute);
        }
        
        const newNumber = '-' + numberAsString;
        return eval(newNumber);
    }
}
// ...
export const Kata = { opposite: n => -n };
// ...
export class Kata {
    static opposite(n: number) {
        return n > 0 ? parseFloat(`-${n}`) : parseFloat(`${n * -1}`);
    }
}
// ...
export class Kata {
    static opposite(n: number) {
        // your code here
        return n > 0 ? Number("-".concat(n.toString())) : Number(n.toString().slice(1,));
    }
}