// https://www.codewars.com/kata/jaden-casing-strings/train/javascript
// My solution
String.prototype.capitalize = function () {
    const first = this.charAt(0).toUpperCase();
    const ns = this.slice(1);
    return first + ns;
}

String.prototype.toJadenCase = function () {
    return this.split(" ")
        .map(str => str.capitalize())
        .join(" ");
};

// ...
String.prototype.toJadenCase = function () {
    return this.split(" ").map(function(word){
        return word.charAt(0).toUpperCase() + word.slice(1);
    }).join(" ");
}

// ...
String.prototype.toJadenCase = function () {
    // return this.replace(/(^|\s)[a-z]/g, function(x){ return x.toUpperCase(); });
    return this.replace(/(^|\s)[a-z]/g, letterAfterSpace => letterAfterSpace.toUpperCase());
};