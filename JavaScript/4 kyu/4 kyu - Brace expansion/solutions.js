// https://www.codewars.com/kata/597f11f61fe82a80c200002c/solutions/javascript

// ...
function expandBraces(str) {
  const count = (c) => (c == "{" ? 1 : c == "}" ? -1 : 0);
  let start = str.indexOf("{"),
    end = start + 1,
    ctr = 1; // Find first/next `{`   |  Counter used to count nested braces
  if (start < 0) return [str]; // No braces? All done!
  while (ctr) ctr += count(str[end++]); // Iterate thru `str` until find matching `}`

  return [...str.slice(start + 1, end - 1)] // Turn first brace grouping into array of chars
    .map((c) => (!(ctr += count(c)) && c == "," ? ";" : c)) // Mark commas at top level only (replace with `;`)
    .join("")
    .split(";") // Create array of choices
    .map((s) => str.slice(0, start) + s + str.slice(end)) // Map back into orig str
    .reduce((all, some) => all.concat(expandBraces(some)), []); // Recurse in case any more braces (nested or alone)
}

// ...
let expandBraces = (str) => {
  let match = str.match(/{([^{}]*?)}/);

  if (match === null) return [str];

  let [first, ...others] = match[1]
    .split(",")
    .map((s) => expandBraces(str.replace(match[0], s)));

  return first.reduce(
    (acc, s, i) =>
      first.length > 1 && others.every((c) => c[i] === s)
        ? [...acc, s]
        : [...acc, first[i], ...others.map((c) => c[i])],
    []
  );
};
