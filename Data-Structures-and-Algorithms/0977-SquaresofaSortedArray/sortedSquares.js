const sortedSquares = function(nums) {
    var result = [];
    let l = 0;
    let r = nums.length - 1;
    while (l <= r) {
        if (Math.abs(nums[l]) < Math.abs(nums[r])) {
            result.push(nums[r]*nums[r]);
            r --;
        } else {
            result.push(nums[l]*nums[l]);
            l ++;
        }
    }
    return result.reverse()
};

nums = [-16, -7, -1, 0, 3, 7, 9]
console.log(sortedSquares(nums))

// O(n) as it iterates through the whole array (n/2 -> n)
// O(1) for space (constant extra space), if result array is not counted (which it shouldn't)
// Sort the squares of a sorted array 
