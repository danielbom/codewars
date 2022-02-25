// https://www.codewars.com/kata/grasshopper-terminal-game-combat-function-1/train/javascript
// My solution
function combat(health, damage) {
    let result = health - damage;
    return result > 0 ? result : 0;
}
// ...
function combat(health, damage) {
    return health < damage ? 0 : health - damage
}
// ...
const combat = (health, damage) => Math.max(0, health - damage);
