const threeSum = function(nums) {
    let ans = [];
    // impossible to make a 0 out of less than 3 numbers per requested
    if (nums.length < 3) {
        return []
    }
    // Sort the array in increasing (ascending) order.
    nums.sort((a,b) => a - b)
    // Outer for loop
    for (let i = 0; i < nums.length - 2; i++) {
        // Skip numbers that are equal to their immediate predecessors
        if (i > 0 && nums[i] == nums[i-1]) {
            continue
        }
        // With nums[i] in hand, find a twoSum using two pointers approach from two sides of the rest of the array
        let left = i+1;
        let right = nums.length-1;
        while (left < right) {
            let cursum = nums[i] + nums[left] + nums[right]
            if (cursum < 0) {
                left ++;
            } else if (cursum > 0) {
                right --;
            } else if (cursum == 0) { 
                ans.push([nums[i], nums[left], nums[right]])
                while(nums[left]===nums[left+1]){left++}
                while(nums[right]===nums[right-1]){right--}
                left++;
                right--;
            }
        }
    }

    return ans
}

nums = [-1,0,1,2,-1,-4]
console.log(threeSum(nums))
