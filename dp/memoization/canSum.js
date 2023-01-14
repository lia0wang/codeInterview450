const canSum = (targetSum, numbers, memo={}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;

    // iterate the numbers array
    for (let num of numbers) {
        // branching logic, subtract the target number
        const remainder = targetSum - num;
        if (canSum(remainder, numbers, memo) === true) {
            // return true
            // store the new key
            memo[targetSum] = true;
            return true;
        }
    }
    
    // targetSum != 0, not found
    memo[targetSum] = false;
    return false;
}

console.log(canSum(11, [2, 6]));