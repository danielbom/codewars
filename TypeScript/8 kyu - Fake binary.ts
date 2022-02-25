// https://www.codewars.com/kata/fake-binary/train/typescript
// My solution
export const fakeBin = (x:string):string => {
    return x.replace(/[1234]/gi, "0").replace(/[56789]/gi, "1");
};

// ...
export const fakeBin = (x:string):string => x.replace(/\d/g, n => Number(n) < 5 ? '0' : '1');
// ...
export const fakeBin = (x:string):string => {
    var a = x.split('')
    for (var i = 0 ; i < a.length ; i++ )
    {
        if ( parseInt(a[i]) < 5 )
            a[i] = "0"
        else
            a[i] = "1"
    }
    return a.join('')
};
// ...
export const fakeBin = (x:string):string => {
    return x.split('').map(res => Number(res) < 5 ? 0 : 1).join('');
};
// ...
export const fakeBin = (x:string):string => {
    return x.split('').map((item) => Number(item) < 5 ? '0' : '1' ).join('');
};
// ...
export const fakeBin = (x:string):string => {
    return x.replace(/[1-4]/g, '0').replace(/[5-9]/g, '1');
};