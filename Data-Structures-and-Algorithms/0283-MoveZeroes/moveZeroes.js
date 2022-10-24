const moveZeroes = function(nums) {

    inserter = 0;
    reader = 1;

    while (reader < nums.length) {
        if (nums[inserter] != 0) {
            inserter++;
            reader++;
        } else if (nums[inserter] == 0) {
            if (nums[reader]==0) {
                reader ++;
            } else if (nums[reader]!=0) {
                [nums[inserter], nums[reader]] = [nums[reader], nums[inserter]]
                inserter++
            }
        }
    }

    return nums
};

nums = [0,0,1,2,0,5,6,9,14,12,0,1,0]
console.log(moveZeroes(nums))

// # O(2N) ~= O(N)
// O(1)
// Move zeroes to the end of the array