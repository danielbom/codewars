// https://www.codewars.com/kata/snail/train/javascript
// My solution
function snail(array) {
    function move(array, visited, n, i, j, result, direction) {
        if ( i >= n || j >= n || j < 0 || i < 0 ) return ;
        if ( visited[i][j] ) return ;
        visited[i][j] = true;
        result.push(array[i][j]);
        switch(direction) {
            case "right":
                move(array, visited, n, i, j+1, result, direction);
                move(array, visited, n, i+1, j, result, "down");
                break;
            case "down":
                move(array, visited, n, i+1, j, result, direction);
                move(array, visited, n, i, j-1, result, "left");
                break;
            case "left":
                move(array, visited, n, i, j-1, result, direction);
                move(array, visited, n, i-1, j, result, "up");
                break;
            case "up":
                move(array, visited, n, i-1, j, result, direction);
                move(array, visited, n, i, j+1, result, "right");
                break;
        }
    }

    if (array.length == 1 && array[0].length == 0) return [];
    
    let n = array.length;
    let visited = new Array(n).fill(false);
    for (let i = 0; i < n; i++)
        visited[i] = new Array(n).fill(false);
    
    let result = new Array();
    move(array, visited, n, 0, 0, result, "right");
    return result;
}
// ...
snail = function(array) {
    var result;
    while (array.length) {
        // Steal the first row.
        result = (result ? result.concat(array.shift()) : array.shift());
        // Steal the right items.
        for (var i = 0; i < array.length; i++)
            result.push(array[i].pop());
        // Steal the bottom row.
        result = result.concat((array.pop() || []).reverse());
        // Steal the left items.
        for (var i = array.length - 1; i >= 0; i--)
            result.push(array[i].shift());
    }
    return result;
}
// ...
function snail(array) {
    var vector = [];
    while (array.length) {
        vector.push(...array.shift());
        array.map(row => vector.push(row.pop()));
        array.reverse().map(row => row.reverse());
    }
    return vector;
}
// ...
snail = function(array) {
    var maxx = array[0].length,
        maxy = maxx,
        minx = -1, miny = 0,
        x = 0, y = 0,
        result = [], dir = "r";
    
    for(var i = maxx*maxx;i>0;i--){
        result.push(array[y][x]);
        switch (dir){
            case "u": y--; break;
            case "l": x--; break;
            case "d": y++; break;
            case "r": x++; break;
        }
        if(x==maxx-1 && y==miny){ dir="d"; minx++; }
        else if(x==maxx-1 && y==maxy-1){ dir="l"; miny++;  }
        else if(x==minx && y==maxy-1){ dir="u"; maxx--; }
        else if(x==minx && y==miny){ dir="r"; maxy--; }
    }  
    return result;
}
// ...
snail = function(array) {
    var size = array.length;
    
    if (size == 0) return [];
    if (size == 1) return array[0];
    
    var top    = array[0].slice(0, -1);
    var right  = array.slice(0, -1).map(a => a[size - 1]);
    var bottom = array[size -1].slice(1).reverse();
    var left   = array.slice(1).map(a => a[0]).reverse();
    var inner  = array.slice(1, -1).map(a => a.slice(1, -1));
  
    return [].concat(top, right, bottom, left, snail(inner));
}
// ...
const bToT = arr => arr ? arr.map(v => v[0])
  .reverse().concat(snail(arr.map(v => v.slice(1)))) : [];

const rToL = arr => arr[arr.length - 1] ? arr[arr.length - 1]
  .reverse().concat(bToT(arr.slice(0, -1))) : [];

const tToB = arr => arr ? arr.map(v => v[v.length - 1])
  .concat(rToL(arr.map(v => v.slice(0, -1)))) : [];

const lToR = arr => arr[0] ? arr[0].concat(tToB(arr.slice(1))) : [];

const snail = arr => arr ? lToR(arr) : [];
// ...
snail = function(arr) {
    var result = [];
    var top = 0, bottom = arr.length-1;
    var left = 0, right = arr[0].length-1;
    
    do {
        for (var i = left; i <= right; i++)   result.push( arr[top][i] ) // top row
        for (var i = top+1; i <= bottom; i++) result.push( arr[i][right] ) // right column
        for (var i = right-1; i >= left; i--) result.push( arr[bottom][i] ) // bottom row
        for (var i = bottom-1; i > top; i--)  result.push( arr[i][left] ) // left column
        top++; bottom--; left++; right--;
    } while (top <= bottom);
    
    return result;
  }