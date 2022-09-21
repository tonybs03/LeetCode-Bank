var zeroFilledSubarray = function(nums) {
    if (nums.length == 0) {
        return 0
    }
    
    let result = 0;
    let j = 0;
    for (var i=0; i < nums.length; i++) {
        if (nums[i] == 0) {
            result += i - j + 1
        };
        if (nums[i] != 0) {
            j = i + 1
        };
    }
    return result
};

arr = [0,0,0,2,0,0,2,0,0,0]
console.log(zeroFilledSubarray(arr))

// O(N) for time (N steps to iterate through)
// O(N) for space (constant extra space)