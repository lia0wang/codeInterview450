const howSum = (targetSum, numbers, memo={}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum < 0) return null;
    if (targetSum === 0) return [];
    
    for (let n of numbers) {
        const remainder = targetSum - n;
        const remainderResult = howSum(remainder, numbers, memo);
        if (remainderResult !== null) {
            memo[targetSum] = [ ...remainderResult, n];
            return memo[targetSum];
        }
    } 
    memo[targetSum] = null;
    return null;
}

console.log(howSum(300, [7, 14]));