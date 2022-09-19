var height = [1, 8, 9, 5, 1200, 3, 1900, 300, 25];
console.log(height);

const maxArea = function(h) {
    let i = 0;
    let j = h.length - 1;
    let maxarea = 0;
    while(i < j) {
        maxarea = Math.max((maxarea),(Math.min(h[i], h[j]) * (j-i)));
        h[i] <= h[j] ? i++ : j--
    }
    return maxarea
};

console.log(maxArea(height));


// O(N) for time (N/2 steps to iterate through)
// O(1) for space (constant extra space, maxarea stores one information)