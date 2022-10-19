const removeDuplicates = function(nums) {
    let insind = 1;
    for (var i = 1; i < nums.length; i++) {
        if (nums[i] != nums[insind-1]) {
            nums[insind] = nums[i];
            insind ++;
        }
    }
    return insind, nums
};

nums = [0,0,1,1,1,2,2,3,3,4]
console.log(removeDuplicates(nums))

// O(n)
// O(1)
// Remove repeated elements