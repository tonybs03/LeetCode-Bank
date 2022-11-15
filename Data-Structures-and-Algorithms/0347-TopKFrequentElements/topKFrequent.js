const topKFrequent = function(nums, k) {
    // because k is in the range of 1 to number of unique numbers
    if (nums.length == k) {
        return nums
    }
        
    // create a map that records the number as key and count as value (On and On)
    const map = new Map();
    for (const n of nums) {
        if (map[n] == null) {
            map[n] = 1
        } else {
            map[n] ++
        }
    }

    // create a bucketlist with count as the index (index 0 contains numbers that has been repeated once, and index 1....)
    let bucketlist = []
    for (const n of nums) {
        bucketlist.push([])
    }
    for (const [key, value] of Object.entries(map)) {
        bucketlist[value - 1].push(parseInt(key))
    }

    // create a final list that contains all entries of numbers from least to most appeared
    let finalist = []
    for (bucket of bucketlist) {
        finalist.push(...bucket)
    }

    return finalist.slice(-k)
};

var nums = [1, 1, 1, 1, 4, 5, 6, 7, 5, 6, 8, 1, 4, 5, 0, 1, 2, 5, 0, 5, 5, 5, 5, 5, 5, 5, 6]
var k = 3
console.log(topKFrequent(nums, k))

// O(N) for time, because we traverse through the iteration for multiple times but never nested within each other
// O(N) for space for similar reasons
// Top K numbers with the most appearences