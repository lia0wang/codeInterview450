// memoization

const fib = (n, memo = {}) => {
    // Basic cases
    if (n in memo) return memo[n];
    if (n <= 2) {
        return 1;
    }
    
    // Recursion relation
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
}

console.log(fib(6));
console.log(fib(7));
console.log(fib(200));
