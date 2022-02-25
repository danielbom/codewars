// https://www.codewars.com/kata/disemvowel-trolls/train/typescript
// My solution
export class Kata {
    static disemvowel(str: string) {
        return str.replace(/[aeiouAEIOU]/g, '');
    }
}

// ...
export class Kata {
    static disemvowel(str: string) {
        return str.replace(/[aeiou]/gi, "");
    }
}
// ...
export class Kata {
    static disemvowel(str: string) {
        return str.match(/[^aeiou]/gi).join("");
    }
}