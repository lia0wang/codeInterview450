const gridTraveler = (row, col, memo = {}) => {
    const key = [col, row].join(',');

    // are the arguments in the memo?
    if (key in memo) return memo[key];
    if (row == 0 || col == 0) return 0;
    if (row == 1 && col == 1) return 1;
    
    // gT(2,1) == gT(1,2)
    memo[key] = gridTraveler(row - 1, col, memo) + gridTraveler(row, col - 1, memo);
    return memo[key];
}

console.log(gridTraveler(18, 18));