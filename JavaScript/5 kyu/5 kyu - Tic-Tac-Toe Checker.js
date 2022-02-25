// https://www.codewars.com/kata/tic-tac-toe-checker/train/javascript
// My solution
function isSolved(board) {
    let d1 = 0, d2 = 0, nullSpots = 0;
    for (let i = 0; i < 3; i++) {
        d1 +=  board[i][i]  == 1 ? 1 :  board[i][i]  == 2 ? -1 : 0 ;
        d2 += board[i][2-i] == 1 ? 1 : board[i][2-i] == 2 ? -1 : 0 ;
        let clin = 0, ccol = 0;
        for ( let j = 0; j < 3; j++ ) {
            nullSpots += board[i][j] == 0;
            clin += board[i][j] == 1 ? 1 : board[i][j] == 2 ? -1 : 0 ;
            ccol += board[j][i] == 1 ? 1 : board[j][i] == 2 ? -1 : 0 ;
        }
        if ( clin ==  3 || ccol ==  3 ) return 1;
        if ( clin == -3 || ccol == -3 ) return 2;
    }
    if ( d1 ==  3 || d2 ==  3 ) return 1;
    if ( d1 == -3 || d2 == -3 ) return 2;
    if ( nullSpots == 0 ) return 0;
    return -1;
}
// ...
function isSolved(board) {
    board = board.join('-').replace(/,/g,'');
    if(/222|2...2...2|2....2....2|2..2..2/.test(board)) return 2;
    if(/111|1...1...1|1....1....1|1..1..1/.test(board)) return 1;
    if(/0/.test(board)) return -1;
    return 0;
}
