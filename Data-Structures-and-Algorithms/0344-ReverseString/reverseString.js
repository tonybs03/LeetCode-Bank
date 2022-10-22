var arr = ["h","e","l","l","o"];
console.log(arr);

const reverseString = function(s) {
    let left = 0;
    let right = s.length - 1;
    
    while(right > left) {
      let temp =  s[right];
        s[right--] = s[left];
        s[left++] = temp;
    }
    return s
};

console.log(reverseString(arr));
console.log(arr);

// O(N) for time (N/2 swaps)
// O(1) for space (no recursion)
// Two pointer, left end and right end, move inwards.