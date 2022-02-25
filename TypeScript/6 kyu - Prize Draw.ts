// https://www.codewars.com/kata/prize-draw/train/typescript
// My solution
export class G964 {
    public static rank(st, we, n) {
        if (we.length < n) return "Not enough participants";

        const names = st.split(',');                // Spliting names
        if (names.length == 0) return "No participants";
        if (we.length != names.length) return "No participants";

        const weights = st.toLowerCase().split(',') // Creating a array with weights
            .map((name, index) => {
                const weight = name.split('')
                    .map(char => char.charCodeAt(0) - 96)
                    .reduce((a, b) => a + b);
                return (weight + name.length) * we[index];
            });

        const zipped = [] // Zip the names with weights
        for (var i = 0; i < names.length; i++)
            zipped.push([names[i], weights[i]]);

        zipped.sort((a, b) => { // Sorting the zipped array
            const cmp = <number>b[1] - <number>a[1];
            if (cmp == 0) {       // If the weights is equals, sort by name
                const name1 = <string>a[0];
                const name2 = <string>b[0];
                return name1.localeCompare(name2);
            }
            return cmp;
        });
        return <string>zipped[n - 1][0];
    }
}
// ...
export class G964 {

    public static rank(st, we, n) {
        if (st == null || st.length === 0) return 'No participants';
        let names: string[] = st.split(',');
        if (n > names.length) return 'Not enough participants'

        class Record {
            constructor(readonly name: string, readonly score: number) { }

            static compare(a: Record, b: Record) {
                const diff: number = b.score - a.score;
                return diff == 0 ? a.name.localeCompare(b.name) : diff;
            }
        }

        let data: Record[] = [];
        for (let i: number = 0; i < names.length; i++) {
            const name: string = names[i];
            const csum: number = name.toUpperCase().split('').map(c => { return c.charCodeAt(0) - 64 }).reduce((acc, val) => { return acc + val });
            data.push(new Record(name, we[i] * (name.length + csum)));
        }

        data.sort(Record.compare);

        return data[n - 1].name;
    }
}
// ...
export class G964 {

    public static rank(st, we, n) {
        if (!st) {
            return 'No participants'
        }

        const names: string[] = st.split(',')
        if (n > names.length) {
            return 'Not enough participants'
        }

        const winNumber: number[] = names.map((name, idx) =>
            we[idx] * (name.length + name.split('').reduce((sum, c) => sum + c.toLowerCase().charCodeAt(0) - 96, 0))
        )

        return names.map((name, idx) => [name, winNumber[idx]])
            .sort((a, b) => a[1] === b[1] && (a[0] < b[0] && -1 || 1) || a[1] > b[1] && -1 || 1)[n - 1][0]
    }
}
// ...
export class G964 {
    public static rank(st, we, n) {
        return st ? st.split(',')
            .map((name, i) => {
                const str = name.toLowerCase();
                return {
                    name: name,
                    val: (str.length + str.split('').reduce((p, c) => p + (c.charCodeAt(0) - 96), 0)) * we[i]
                }
            })
            .sort((a, b) => (b.val - a.val) || a.name.localeCompare(b.name))
            .map(o => o.name)[--n]
            || 'Not enough participants'
            : 'No participants';
    }
}
// ...
/*** The unweighted name score. */
export const score = (name: string): number => {
    const nameLower = name.toLowerCase()
    let score = 0
    for (let i = 0; i < nameLower.length; i++) {
        score += nameLower.charCodeAt(i) - 96
    }
    return score + nameLower.length
}

/*** Score and weight each name. */
export const weightedScores = (names: Array<string>, weights: Array<number>): Array<number> => {
    let scores = []
    for (let i = 0; i < names.length; i++) {
        scores.push(score(names[i]) * weights[i])
    }
    return scores
}

/*** Create a map of score to names. It's possible for names to have the same score, so each value is a sorted array of names. */
export const mapByScore = (names: Array<string>, scores: Array<number>): Map<number, Array<string>> => {
    const map = new Map()
    for (let i = 0; i < names.length; i++) {
        const n = names[i]
        const s = scores[i]
        const v = map[s]
        if (typeof v === 'undefined') {
            map[s] = [n]
        } else {
            v.push(n)
            v.sort()
        }
    }
    return map
}

export class G964 {
    public static rank(names: string, weights: Array<number>, pick: number): string {
        if (!names || names.trim().length === 0) {
            return 'No participants'
        }
        const namesArray = names.split(',')
        if (pick > namesArray.length) {
            return 'Not enough participants'
        }
        const scores = weightedScores(namesArray, weights)
        const scoreMap = mapByScore(namesArray, scores)
        const rankedScores = [...scores].sort((a, b) => b - a)
        const rankedNames = rankedScores.map(s => scoreMap[s].shift())
        return rankedNames[pick - 1]
    }
}