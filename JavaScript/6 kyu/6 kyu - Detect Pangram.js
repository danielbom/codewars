// https://www.codewars.com/kata/detect-pangram/train/javascript
// My solution
function isPangram(string){
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    const lower = string.toLowerCase();
    for (let ch of alphabet) {
        if (!lower.includes(ch)) {
            return false;
        }
    }
    return true;
}

// ...
function isPangram(string){
    string = string.toLowerCase();
    return "abcdefghijklmnopqrstuvwxyz".split("").every(function(x){
        return string.indexOf(x) !== -1;
    });
}

// ...
function isPangram(string){
    return (string.match(/([a-z])(?!.*\1)/ig) || []).length === 26;
}

// ...
function isPangram(string){
    return 'abcdefghijklmnopqrstuvwxyz'
        .split('')
        .every((x) => string.toLowerCase().includes(x));
}

// ...
function isPangram(string){
    const str = string.replace(/[^a-zA-Z]/gi,'').toLowerCase()
    const set = new Set([...str]);
    return set.size === 26;
}

// ...
function isPangram(string) {
    return new Set(string.toLocaleLowerCase().replace(/[^a-z]/gi, '').split('')).size === 26;
}

// ...
function isPangram(str) {
    letters: for (var c = 0; c < 26; c++) {
        for (var i = 0; i < str.length; i++) {
            var s = str.charCodeAt(i)
            if (s < 65 || s > 90 && s < 97 || s > 122) continue
            if (s === 65 + c || s === 97 + c) continue letters
        }
        return false
    }
    return true
}