const reverseWords = function(s) {
    // split the string by space into an array O(N)
    let arr = s.split(' ');
    let res = '';
    // iterate backwards through the array O(N)
    for (var i = arr.length-1; i >= 0; i--) {
        // if the element is a word, add the word to the string 
        if (arr[i] != '') {
            // if is not the first word, add a space before the word to avoid trimming
            if (res.length > 0) {
                res += " "
            }
            res += arr[i]
        } 
    }
    return res
};

s = " the sky is blue "
console.log(reverseWords(s))