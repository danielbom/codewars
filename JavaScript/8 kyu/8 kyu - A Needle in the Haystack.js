// https://www.codewars.com/kata/a-needle-in-the-haystack/train/javascript
// My solution
function findNeedle(haystack) {
    return 'found the needle at position ' + haystack.findIndex(x => x == 'needle')
}

// ...
function findNeedle(haystack) {
    return "found the needle at position " + haystack.indexOf("needle");
}

// ...
const findNeedle = haystack => `found the needle at position ${haystack.indexOf('needle')}`;

