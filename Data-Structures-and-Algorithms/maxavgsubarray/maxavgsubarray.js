var findMaxAverage = function(nums, k) {
    let cursum = 0;
    let maxsum = 0;
    for (var i = 0; i < k; i++) {
        cursum += nums[i];
    };
    maxsum = cursum;
    for (var j = k; j < nums.length; j++) {
        cursum += nums[j] - nums[j-k]
        maxsum = Math.max(maxsum, cursum);
    };
    
    return maxsum*1.0/k;
};

var arr = [-1];
var k  = 1

console.log(findMaxAverage(arr, k));
console.log(arr);

// O(N) for time (N/2 swaps)
// O(1) for space (no recursion)
