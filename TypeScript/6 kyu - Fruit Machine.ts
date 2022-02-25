// https://www.codewars.com/kata/fruit-machine/train/typescript
// My solution
export function fruit(reels: string[], spins: number[]): number {
    function swap(result: string[], i: number, j: number) {
        const tmp = result[i];
        result[i] = result[j];
        result[j] = tmp;
    }
    // Creating the score table
    const items = "Wild Star Bell Shell Seven Cherry Bar King Queen Jack";
    const scoring = {};
    items.split(" ").forEach((val, index) => {
        const score = 10 - index;
        scoring[val] = { 3: score * 10, 2: score };
    });
    const r = [reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]];
    // Separating the discriminant
    if (r[0] == r[1]) swap(r, 0, 2);
    else if (r[0] == r[2]) swap(r, 0, 1);
    // Evaluating the result
    const count = (r[0] === r[1] ? 1 : 0) + (r[1] === r[2] ? 1 : 0) + (r[0] === r[2] ? 1 : 0);
    if (count == 3) return scoring[r[1]]["3"];
    if (count == 1) return scoring[r[1]]["2"] * (r[0] === "Wild" ? 2 : 1);
    return 0;
}
// ...
export function fruit(reels: string[], spins: number[]): number {
    const item: string[] = ['Jack', 'Queen', 'King', 'Bar', 'Cherry', 'Seven', 'Shell', 'Bell', 'Star', 'Wild'];
    const symbol: string[] = [reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]].sort();

    if (symbol.filter(n => n === symbol[0]).length === 3) {
        return (item.indexOf(symbol[0]) + 1) * 10;
    }
    if (symbol[0] === symbol[1] && symbol[2] === 'Wild') {
        return (item.indexOf(symbol[1]) + 1) * 2;
    }
    if (symbol[0] === symbol[1] || symbol[1] === symbol[2]) {
        return item.indexOf(symbol[1]) + 1;
    }
    return 0;
}