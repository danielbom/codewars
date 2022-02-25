// https://www.codewars.com/kata/remove-string-spaces/train/typescript
// My solution
export function noSpace(x:string):string {
    return x.replace(/ /g, "");
}

// ...
export function noSpace(x:string):string {
    return x.replace(/\s/g, '');
}
// ...
export function noSpace(x:string):string {
    return x.replace(new RegExp(' ', 'g'), '');
}