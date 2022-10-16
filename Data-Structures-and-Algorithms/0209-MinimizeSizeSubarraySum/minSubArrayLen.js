const minSubArrayLen = function(target, nums) {
    let left = 0;
    let right = 0;
    let cursum = 0;
    let ans = Infinity;

    for (var i=0; i < nums.length; i++) {
        cursum += nums[i]
        right = i;
        while (cursum >= target) {
            ans = Math.min(right - left + 1, ans)
            cursum -= nums[left];
            left ++;
        }
    }
    return (ans == Infinity)? 0 : ans
};

// O(n) single iteration through n elements
// O(1) for space (constant extra space)
// Return minimal length of continuous elements with sum bigger and equal to the target
