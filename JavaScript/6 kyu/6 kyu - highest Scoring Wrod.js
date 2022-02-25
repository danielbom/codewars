// https://www.codewars.com/kata/highest-scoring-word/train/javascript
// My solution
function high(x){
    return x.toLowerCase().split(" ").reduce((max, cur) => {
        const score = cur.split("").reduce((sum, ch) => ch.charCodeAt(0) - 96 + sum, 0);
        return max.score >= score ? max : { score: score, string: cur };
    }, { score: 0, string: ""}).string;
}

// ...
function high(x){
    //transform the input string into array & define a string of alphabetical latin characters
    var arr = x.split(' ');
    var str = 'abcdefghijklmnopqrstuvwxyz';
    //Iterate through the array with input words to find the one with the greatest sum
    var newArr = arr.map(function(word){
        var sum = 0;
        for (var i = 0; i < word.length; i++) {
            sum += str.indexOf(word[i]);
        }
        return sum;
    });
    //Return the word with the greatest sum
    return arr[newArr.indexOf(Math.max(...newArr))];
}

// ...
function high(s){
    let as = s.split(' ').map(s=>[...s].reduce((a,b)=>a+b.charCodeAt(0)-96,0));
    return s.split(' ')[as.indexOf(Math.max(...as))];
}

// ...
const { compose, reduce, split } = require('ramda');

const score = compose(
    reduce((r, v) => r + v.charCodeAt() - 96, 0),
    split('')
);

const high = compose(
    reduce((r, v) => score(v) > score(r) ? v : r, ''),
    split(' ')
);

// ...
function high(words) {

    const alpha = ' abcdefghijklmnopqrstuvwxyz';
    const score = word => word.split('').reduce((a, b) => a + alpha.indexOf(b), 0);
  
    return words
      .split(' ')
      .map((word, pos) => ({ word: word, pos: pos, score: score(word) }))
      .sort((a, b) => a.score - b.score || b.pos - a.pos)
      .pop()
      .word;
      
}

// ...
function high(x){
    return x.split(' ').reduce((accum, current)=>{
        return score(current) > score(accum)? current:accum;  
    })
}

function score(word){
    return word.split('').reduce((accum,current)=>{return accum+(current.charCodeAt()-96)},0)
}