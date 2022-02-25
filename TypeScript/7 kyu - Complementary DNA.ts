// https://www.codewars.com/kata/complementary-dna/train/typescript
// My solution
export class Kata {
    static dnaStrand(dna: string) {
        const map = { "A": "T", "T": "A", "C": "G", "G": "C" };
        return dna.split("").map(symbol => map[symbol]).join("");
    }
}
// ...
export class Kata {
    static dnaStrand(dna: string) {
        return dna.replace(/./g, (c) => ({ A: 'T', T: 'A', G: 'C', C: 'G' })[c]);
    }
}
// ...
interface IDictionary {
    [index: string]: string;
}

var params: IDictionary = {};
params['A'] = 'T';
params['T'] = 'A';
params['G'] = 'C';
params['C'] = 'G';

export class Kata {
    static dnaStrand(dna: string) {
        let result: string = "";
        let arrayLength: number = dna.length;
        let i: number = 0;

        for (i = 0; i < arrayLength; i++) {
            result = result + params[dna[i]];
        }

        return result;
    }
}
// ...
export class Kata {
    static dnaStrand(dna: string): string {
        const match = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }
        return Array.from(dna, v => match[v]).join('');
    }
}
// ...
export class Kata {
    static dnaStrand(dna: string) {
        return dna.split('').map(c => map.get(c)).join('');
    }
}

export const map: Map<string, string> = new Map<string, string>()
    .set('A', 'T')
    .set('C', 'G')
    .set('G', 'C')
    .set('T', 'A');
// ...
export class Kata {
    static dnaStrand(dna: string) {
        let complement = { "A": "T", "T": "A", "C": "G", "G": "C" };
        return dna.replace(/[atcg]/gi, m => complement[m]);
    }
}
// ...
export class Kata {
    static dnaStrand(dna: string) {
        //your code here
        const CODES = { A: 'T', T: 'A', C: 'G', G: 'C' };
        return dna.split('').map(n => CODES[n]).join('');
    }
}
