// https://www.codewars.com/kata/exclusive-or-xor-logical-operator/train/c
// My solution
int xor(int a, int b) {
    return (a && !b) || (!a && b);
}
// ...
int xor(int a, int b) {
    return a ^ b;
}
// ...
int xor(int a, int b) {
    return a != b;
}
