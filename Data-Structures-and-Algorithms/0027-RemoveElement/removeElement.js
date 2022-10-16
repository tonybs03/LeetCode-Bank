const removeElement = function(nums, val) {
    let count = 0;
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] != val) {
            nums[count] = nums[i];
            count ++;
        }
    }
    return count, nums
};

nums = [1, 2, 2, 2, 5, 7, 9, 11, 2, 19]
val = 2
console.log(removeElement(nums, val))

// O(N)
// O(1) for space (constant extra space)
// remove elements with value val, return number of left over elements