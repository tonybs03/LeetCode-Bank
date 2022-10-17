const intersection = function(nums1, nums2) {
    // return empty if both input arrays are empty
    if (nums1.length === 0 && nums2.length === 0) {
        return []};
    
    // sort through the two arrays to make them sorted
    nums1.sort(function(a, b){return a - b})
    nums2.sort((a, b) => a - b)

    // loop through the two arrays
    let i = 0; 
    let j = 0;
    let ans = [];

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            i++;
        } else if (nums1[i] > nums2[j]) {
            j++;
        } else {
            if (ans.length == 0 || nums1[i] != ans[ans.length - 1]) {
                ans.push(nums1[i])
            };
            i++;
            j++;
        }
    }
    return ans

};

nums1 = [3, 7, 11, 15, 21, 91, 125, 786, 1230] 
nums2 = [5, 7, 0, 8, 12, 156, 78, 11, 3] 
console.log(intersection(nums1, nums2))

// O(mlogm + nlogn) (or O(n)???)
// O(1) for space (constant extra space for ans doesn't count)
// Search the same values from two arrays and return them