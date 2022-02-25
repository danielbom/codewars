// https://www.codewars.com/kata/rainfall/train/typescript
// My solution
export class G964 {
    public static avg = (array) => {
        console.log(array);
        return array.reduce((a, b) => a + b) / array.length || -1;
    }
    public static var = (array) => {
        if (array.length == 0) return -1;
        const avgr = G964.avg(array);
        return array
            .map(val => Math.pow(val - avgr, 2))
            .reduce((a, b) => a + b) / array.length;
    }
    public static mean = (town, strng) => {
        const all_data = strng.split("\n").map(d => d.split(":"));
        const town_data = all_data.find(d => d[0] == town);
        if (town_data == null) return -1;
        const data = town_data[1].split(",").map(d => Number(d.split(" ")[1]));
        return G964.avg(data);
    }
    public static variance = (town, strng) => {
        const all_data = strng.split("\n").map(d => d.split(":"));
        const town_data = all_data.find(d => d[0] == town);
        if (town_data == null) return -1;
        const data = town_data[1].split(",").map(d => Number(d.split(" ")[1]));
        return G964.var(data);
    }
}
// ...
export class G964 {
    private static getNumbers(town: string, data: string): number[] {
        const dataByTown: any = {};
        data.split('\n').forEach(r => {
            const t: string[] = r.split(':');
            dataByTown[t[0]] = t[1].split(',');
        });
        return (dataByTown[town] || []).map(d => +d.split(' ')[1]);
    };

    private static meanFromNumbers(data: number[]): number {
        return data.length === 0 ? -1 : data.reduce((a, v) => a + v, 0) / data.length;
    };

    private static varianceFromNumbers(data: number[]): number {
        if (data.length === 0) { return -1; }
        const mean: number = G964.meanFromNumbers(data);
        return data.map(v => v - mean).reduce((a, v) => a + v * v, 0) / data.length;
    };

    public static mean(town: string, str: string): number {
        return G964.meanFromNumbers(G964.getNumbers(town, str));
    };

    public static variance(town: string, str: string): number {
        return G964.varianceFromNumbers(G964.getNumbers(town, str));
    };
}
// ...
export class G964 {
    public static getValues = (town, data) => {
        const r = new RegExp(town + ":.*", "g");
        return ((r.exec(data) || [""])[0].match(/\d+.\d+/g) || []).map(c => Number(c));
    }
    public static mean = (town, data) => {
        const records = G964.getValues(town, data);
        return records.length > 0 ? records.reduce((a, b) => a + b) / 12 : -1;
    }
    public static variance = (town, data) => {
        const records = G964.getValues(town, data);
        const mean = G964.mean(town, data);
        return records.length > 0 ? records.map(c => (c - mean) ** 2).reduce((a, b) => a + b) / 12 : -1;
    }
}
// ...
export class G964 {
    public static mean = (town, strng) => {
        const data = G964.getData(strng);
        const cityData = data[town];
        if(!cityData) return -1;
        return cityData.reduce((acc, x) => acc + x, 0) / cityData.length;
    }
    public static variance = (town, strng) => {
        const data = G964.getData(strng);
        const cityData = data[town];
        if(!cityData) return -1;
        const mean = G964.mean(town, strng);
        return cityData.reduce((acc, x) => acc + Math.pow(x - mean, 2), 0) / cityData.length;
    }
    private static getData(data){
      const rows = data.split('\n');
      return rows.reduce((acc, x) => {
        const split = x.split(':');
        acc[split[0]] = split[1].split(',').map(x => parseFloat(x.split(' ')[1]));
        return acc;
      }, {});
    }
}