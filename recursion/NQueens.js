//main function
function solveNQueens(n) {
    let res = [];
    solver(0, new Array(), n, res);
    printSolution(res);
}

//皇后的放置方式是以"行"為順序，每一次都在一個行放一個皇后，這樣可以直接排除同個皇后在同一行的情況
function solver(curRow, colPlacements, n, res) {
    //recursion的終止點(已放到最後一行)，繪製棋盤表
    if (curRow == n) {
        let board = generateBoard(n, colPlacements);
        res.push(board);
        return;
    }

    //試著把皇后放到當前行的不同列
    for (let col = 0; col < n; col++) {
        //紀錄目前放的是在哪個列，至於行數就以index做紀錄
        colPlacements.push(col);

        //放置成功，接著前往下一行，繼續放皇后
        if (isValid(colPlacements)) {
            solver(curRow + 1, colPlacements, n, res);
        }

        //如果棋盤上的皇后會互相攻擊，回復(undo)這次的移動，接著試放在下一列
        colPlacements.pop();
    }
}

function generateBoard(n, colPlacements) {
    let board = [];
    for (let row = 0; row < colPlacements.length; row++) {
        let boardRow = [];
        for (let col = 0; col < n; col++) {
            if (col === colPlacements[row]) {
                boardRow.push("Q");
            } else {
                boardRow.push(".");
            }
        }

        board.push(boardRow.join(""));
    }
    return board;
}


//檢查當前皇后位置是否安全，會檢查已放置的皇后，檢查是否有其他皇后和他在同一列或者斜對角
function isValid(colPlacement) {
    let n = colPlacement.length;
    let curRow = n - 1;

    //因為一行放一個，所以還沒放到的行數不必檢查
    for (let row = 0; row< curRow; row++) {
    //(colDistance === 0)檢查是否有其他皇后和他同一列
    //(rowDistance === colDistance)檢查是否有其他皇后在斜對角
        let colDistance = Math.abs(colPlacement[curRow] - colPlacement[row]);
        let rowDistance = curRow - row;
        if (colDistance === 0 || rowDistance === colDistance) {
            return false;
        }
    }

    return true;
}

function printSolution(res) {
    for (let i = 0; i < res.length; i++) {
        console.log(`Solution ${i+1}`);
        console.log(res[i].join("\n"));
        console.log("\n");
    }
}

//test cases
let ans4 = solveNQueens(4);
let ans8 = solveNQueens(8);
