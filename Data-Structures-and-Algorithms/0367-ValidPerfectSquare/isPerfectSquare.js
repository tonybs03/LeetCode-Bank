const isPerfectSquare = function(num) {
    // if num is 1, then it is definitely a perfect square 
    if (num == 1) {
        return true;
    }

    // binary search based on the value of the mid point, from 2 and 
    let left = 2; 
    let right = num; 
    let mid = 0;

    while (left <= right) {
        mid = Math.floor((left + right) / 2)
        if (mid*mid == num) {
            return true;
        } else if (mid*mid < num) {
            left = mid + 1
        } else if (mid*mid > num) {
            right = mid - 1
        }
    }
    
    return false;
};

num = 196
console.log(isPerfectSquare(num))

// O(logn) with log base 2 for it is a binary search
// O(1) for space (constant extra space)
// Determine the validity of a number in terms of being a perfect square