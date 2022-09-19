var tribonacci = function(n) {
    const helper = (n, hashmap = {}) => {
        if (n in hashmap) {
            return hashmap[n]
        }
        else if (n == 2) {
            return 1
        }
        else if (n < 2) {
            return n
        }
        else {
            hashmap[n] = helper(n - 1) + helper(n - 2, hashmap) + helper(n - 3, hashmap)
            return hashmap[n]
        }
    };
    
    return helper(n)
};