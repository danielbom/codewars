// https://www.codewars.com/kata/5ecc1d68c6029000017d8aaf/train/javascript
// My solution
function maxHexagonBeam(n, seq) {
  const sum = ar => ar.reduce((curr, acc) => curr + acc, 0);
  const zeros = n => Array.from({ length: n }, () => 0);
  const transpose = mat => mat.map((_, i) => mat.map((row) => row[i]).filter(k => k));
  const padTop = (top) => top.map((row, i) => zeros(pad - i).concat(row));
  const padBottom = (bottom, zs = 1) => bottom.map(row => zeros(zs++).concat(row));
  const pad = n - 1;
  
  const top = [];
  let k = 0;
  let diag = n;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n + i; j++) {
      if (!top[i]) top[i] = [];
      top[i].push(seq[k % seq.length]);
      k++;
    }
    diag = Math.max(diag, n + i);
  }
  const bottom = [];
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < diag - i - 1; j++) {
      if (!bottom[i]) bottom[i] = [];
      bottom[i].push(seq[k % seq.length]);
      k++;
    }
  }
  
  return Math.max(
    ...top.map(sum),
    ...bottom.map(sum),
    ...transpose([...padTop(top), ...bottom]).map(sum),
    ...transpose([...top, ...padBottom(bottom)]).map(sum),
  );
}

// ...
const maxHexagonBeam = (n, seq) => {
	let n2 = n * 2 - 1,
		sums = Array(n2 * 3).fill(0),
		elFrom = (elCur = 0),
		elTo = n;
	for (let i = 0; i < n2; i++) {
		for (let j = elFrom; j < elTo; j++) {
			sums[i] += seqEl = seq[elCur % seq.length];
			sums[n2 + j] += seqEl;
			sums[n2 * 2 + (n - 1) + (i - j)] += seqEl;
			elCur++;
		}
		i < n - 1 ? elTo++ : elFrom++;
	}
	return sums.reduce((max, e) => Math.max(max, e), -Infinity);
}