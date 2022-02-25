// https://www.codewars.com/kata/replace-with-alphabet-position/train/javascript
// My solution
function alphabetPosition(text) {
    return !text.match("[a-zA-Z]") ? "" : text
        .toLowerCase()
        .match(/[a-z]/g)
        .map(ch => ch.charCodeAt(0) - 96)
        .join(" ")
}

// ...
function alphabetPosition(text) {
    return text
        .toUpperCase()
        .match(/[a-z]/gi)
        .map( (c) => c.charCodeAt() - 64)
        .join(' ');
}

// ...
let alphabetPosition = (text) => text
    .toUpperCase()
    .replace(/[^A-Z]/g, '')
    .split('')
    .map(ch => ch.charCodeAt(0) - 64)
    .join(' ');
