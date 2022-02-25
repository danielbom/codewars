// https://www.codewars.com/kata/string-ends-with/train/typescript
// My solution
export function solution(str: string, ending: string): boolean {
    return !!str.match(new RegExp(`${ending}$`));
}

// ...
export function solution(str: string, ending: string): boolean {
    return str.endsWith(ending);
}
// ...
export function solution(str: string, ending: string): boolean {
    return new RegExp(ending + '$').test(str);
}
// ...
export const solution = Function.prototype.call.bind(String.prototype.endsWith);
// ...
export function solution(str: string, ending: string): boolean {
    for (let i: number = str.length - ending.length, j = 0; i < str.length; ++i, ++j) {
        if (str[i] !== ending[j]) { return false; }
    }
    return true;
}
// ...
export function solution(str: string, ending: string): boolean {
    return str.slice(-ending.length) === ending;
}
// ...
export function solution(str: string, ending: string): boolean {
    return str.substr(-ending.length) == ending;
}
// ...
export const solution = (str: string, ending: string) => str.slice(-ending.length) === ending;
