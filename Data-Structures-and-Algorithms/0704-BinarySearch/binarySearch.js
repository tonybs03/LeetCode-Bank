const binarySearch = function(nums, target) {
    let l = 0;
    let r = nums.length - 1;

    while (l <= r) {
        mid = Math.floor((l + r)/2);
        if (nums[mid] < target) {
            l = mid + 1;
        } else if (nums[mid] > target) {
            r = mid - 1;
        } else {
            return mid;
        }
    }; 

    return -1;
};

nums = [3, 7, 11, 15, 21, 91, 125, 786, 1230]
target = 125
console.log(binarySearch(nums, target))

// O(logN) with log base 2
// O(1) for space (constant extra space)
// Search from left and right, discard half based on sorted array
