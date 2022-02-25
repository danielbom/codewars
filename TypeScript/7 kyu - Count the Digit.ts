// https://www.codewars.com/kata/count-the-digit/train/typescript
// My solution
export class G964 {
    public static nbDig(n, d) {
        var count = 0;
        for (var i = 0; i <= n; i++) {
            var match = (i * i).toString().match(new RegExp(`${d}`, "gi"));
            count += match ? match.length : 0;
        }
        return count;
    }
}

// ...
export class G964 {
    public static nbDig(n, d) {
        let count = 0;
        const regex = new RegExp(`[${d}]`, 'ig');
        for (let i = 0; i <= n; i++) {
            const square = i * i + '';
            const tempCount = square.match(regex);
            count += tempCount ? tempCount.length : 0;
        }
        return count;
    }
}
// ...
export class G964 {
    public static nbDig(n, d) {
        return ([...Array(n + 1).keys()]
            .map(num => num * num)
            .filter(num => num.toString().includes(d)).join(''))
            .split(d).length - 1;
    }
}
// ...
export class G964 {
    public static nbDig(n, d) {
        let contador = 0;

        Array.from({ length: n + 1 }, (v, i) => i)
            .map((e) => Math.pow(e, 2))
            .forEach((e) => contador += (String(e).split(String(d)).length - 1));

        return contador;
    }
}
// ...
export class G964 {
    public static nbDig(n, d) {
        let numArr = [];
        for (let i = 0; i <= n; i++) {
            numArr.push(i ** 2);
        }
        return numArr.join("").split("").filter(e => { return e === d.toString() }).length;
    }
}
// ...
export class G964 {
    public static nbDig(n: number, d: number): number {
        let count: number = 0;
        for (let k: number = 0; k <= n; k++) {
            count += (k * k).toString().split(d.toString()).length - 1;
        }
        return count;
    }
}