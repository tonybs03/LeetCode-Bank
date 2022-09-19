const longestOnes = function(nums, k) {
    let l = 0;
    let r = 0;
    let zeroes = 0;
    let maxlen = 0;
    
    if (nums.length == 0) {
        return 0
    }

    while (r < nums.length) {
        if (nums[r] == 0) {
            zeroes++;
            k--;
        };
        while (k < 0) {
            if (nums[l] == 0) {
                k++;
            }
            l++;
        };
        r++;
        maxlen = Math.max(maxlen, (r - l * 1.0));
        
    }; 
    return maxlen
};

arr = [0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1]
k = 3
console.log(longestOnes(arr,k))

// O(N) for time (N steps to iterate through)
// O(1) for space (constant extra space)



