// https://www.codewars.com/kata/average-scores/train/typescript
// My solution
export function average(scores:number[]):number {
    return Math.round(scores.reduce((a,b) => a+b) / scores.length); 
}
// ...
export function average(scores:number[]):number {
    return Math.round(eval(scores.join("+"))/scores.length);
}