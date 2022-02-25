// https://www.codewars.com/kata/number-shortening-filter/train/javascript
// My solution
function shortenNumber(suffixes, base) {
    return function shortenWith(value) {
        const s = suffixes;
        const b = base;
        
        if (typeof value === 'string') {
            if (value.match(/[^0-9]/) || value === '') return value;
            else value = +value;
        }
        if (typeof value !== 'number') return ""+value;
        
        let i = 1;
        let div = Math.trunc(value / b);
        while (div > 0 && i < s.length) {
            i++;
            div = Math.trunc(value / Math.pow(b, i));
        }
        i--;
        return "" + Math.trunc(value / Math.pow(b, i)) + s[i];
    }
}
// ...
function shortenNumber(suffixes, base) {
    return function(str){
        var count=0;
        while(str>base){
            str=Math.floor(str/base);
            count++;
            if(count>suffixes.length-2)break;
        }
        return str+suffixes[count]
    }
    }
// ...
function shortenNumber(suffixes, base) {
    return function(string) {
        //takes a numerical string and reduces it putting the proper suffix behind it
        //if input is not a numeric string, it is reterned unchanged or converted into string
        if (typeof string!='string' || !/^[0-9]+$/.test(string)) return string.toString();
        //if we need it for extra suffixes, we might just add items to the list
        var i = suffixes.length, n = +string;
        while (i) {
            var divisor = Math.pow(base, --i);
            if (n>=divisor) return Math.floor(n/divisor)+suffixes[i];
        }
        return string;
    };
}