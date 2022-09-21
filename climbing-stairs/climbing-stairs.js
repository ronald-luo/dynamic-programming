var climbStairs = function(n) {
    
    const helper = (n, hashmap = {}) => {
        if (n in hashmap) {
            return hashmap[n]
        }
        else if (n < 0) {
            return 0
        }
        else if (n === 0) {
            return 1
        }
        else {
            let temp_sum = helper(n - 1, hashmap) + helper(n - 2, hashmap)
            hashmap[n] = temp_sum
            return temp_sum
        }
    }
    
    return helper(n)
    
};