// https://www.codewars.com/kata/vowel-count/train/typescript
// My solution
export class Kata {
    static getCount(str: string) {
        //return (str.match(/a|e|i|o|u/g) || []).length;
        return (str.match(new RegExp("a|e|i|o|u", "g")) || []).length;
    }
}

// ...
export class Kata {
    static getCount(str: string) {
        let list = str.match(/[aeiou]/gi);
        return list ? list.length : 0;
    }
}
// ...
export class Kata {
    static getCount(str: string) {
        return str.replace(/[^aeiou]/gi, '').length
    }
}
// ...
export class Kata {
    static getCount(str: string) {
        let vowels: string[] = ["a","e","i","o","u"]
        return str.toLowerCase().split("")
            .reduce((a:number,e:string)=>{
                if(vowels.indexOf(e) > -1) a += 1
                return a
            },0)
    }
}
// ...
export class Kata {
    static getCount(str: string) {
        let count = 0;
        const vowels = ["a", "e", "i", "o", "u"];

        for (let i = 0; i < str.length; i++){
            for (let vowel of vowels){
                if (vowel == str[i].toLowerCase()){
                    count++
                }
            }
        }
        return count;
    }
}
// ...
export class Kata {
    static getCount(str: string) : number {
        return str.split('').filter(c => /[aeiou]/i.test(c)).length
    }
}
// ...
export class Kata {
    static getCount(str: string) {
        // your code here
        const vowels: string = 'aeiou';
        let count = 0;
        [...str].forEach((ch: string) => {
            if (vowels.indexOf(ch) !== -1)
            count++;
        });
        
        return count;
    }
}