const twoSum = function(nums, target) {
    let map = {};
    for (var i=0; i < nums.length; i++) {
        let comp = target - nums[i];
        if (map[comp] !== undefined) {
            return [i, map[comp]]
        } else {
            map[nums[i]] = i;
        }
    }
};

arr = [1, 3, 5, 9, 3, 12, -5, 6, 12]
k = 13
console.log(twoSum(arr,k))

// O(N) for time (N steps to iterate through)
// O(1) for space (constant extra space)

