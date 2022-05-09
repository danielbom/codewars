// https://www.codewars.com/kata/576af5056a3efe4b130020bd/train/javascript
// My solution
const BRAIN = require("brain");
const net = new BRAIN.NeuralNetwork();

const rock = [0, 0, 1];
const paper = [1, 0, 0];
const scissor = [0, 1, 0];

const p2Win = [0, 1];
const p1Win = [1, 0];
const draw = [1, 1];
const play = (p1, p2) => p1.concat(p2);

net.train([
  { input: play(rock, rock), output: draw },
  { input: play(paper, paper), output: draw },
  { input: play(scissor, scissor), output: draw },

  { input: play(rock, scissor), output: p1Win },
  { input: play(scissor, paper), output: p1Win },
  { input: play(paper, rock), output: p1Win },

  { input: play(scissor, rock), output: p2Win },
  { input: play(paper, scissor), output: p2Win },
  { input: play(rock, paper), output: p2Win },
]);

// ...
const BRAIN = require("brain");
const net = new BRAIN.NeuralNetwork();

const [paper, rock, scissors] = [
  [1, 0, 0],
  [0, 0, 1],
  [0, 1, 0],
];
const [lose, win, tie] = [
  [0, 1],
  [1, 0],
  [1, 1],
];

net.train([
  { input: [...paper, ...paper], output: tie },
  { input: [...paper, ...rock], output: win },
  { input: [...paper, ...scissors], output: lose },
  { input: [...rock, ...rock], output: tie },
  { input: [...rock, ...scissors], output: win },
  { input: [...rock, ...paper], output: lose },
  { input: [...scissors, ...scissors], output: tie },
  { input: [...scissors, ...paper], output: win },
  { input: [...scissors, ...rock], output: lose },
]);
