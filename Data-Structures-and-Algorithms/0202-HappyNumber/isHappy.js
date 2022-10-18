const isHappy = function(n) {

    const nextnum = function(n) {
        let sum = 0;
        var arr = Array.from(String(n), Number);
        for (var i=0; i<arr.length; i++) {
            sum += (arr[i]*arr[i]);
        }
        return sum
    }

    slow = n;
    fast = nextnum(n);
    while (fast != 1 && slow != fast) {
        slow = nextnum(slow);
        fast = nextnum(nextnum(fast));
    }

    return fast == 1
};

n = 19
console.log(isHappy(n))

// O(logN) with log base 10
// O(1) since no extra hashset or hashmap needed
// Sum of each digit squared of a number, recursive, until number is 1 