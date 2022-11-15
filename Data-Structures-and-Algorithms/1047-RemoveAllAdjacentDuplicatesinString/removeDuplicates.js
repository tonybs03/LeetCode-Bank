// Solution using stack track
const removeDuplicates = function(s) {
    // initiate the resulting array of characters to be joined
    const res = [];
    // for each character of string s
    for (var ch of s) {  
        if (ch == res[res.length-1]) {
            res.pop()
        } else {
            res.push(ch)
        }
    }
    // join the array elements with nothing inbetween
    return res.join('')
};

S = 'aabbccioppoilaabbpweiqwoebcasjjjdal'
console.log(removeDuplicates(S))

// O(N) for time, because we traverse once through the string of length N
// O(N) for space, we store the res as array then join
// Remove all adjacent repeating elements