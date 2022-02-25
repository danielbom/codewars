// https://www.codewars.com/kata/exclamation-marks-series-number-1-remove-a-exclamation-mark-from-the-end-of-string/train/typescript
// My solution
export function remove(s: string): string {
    var n = s.length-1;
    return s.charAt(n) == '!' ? s.slice(0,n) : s;
}

// ...
export const remove = (s: string): string => s.replace(/!$/, '')
