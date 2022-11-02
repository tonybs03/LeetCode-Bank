var isValid = function(s) {
    // make a hashmap first for storing the bracket types
    const refmap = {'(': ')', '{': '}', '[': ']'};
    // make the stack
    const stack = [];
    // for each character in the string
    for (var i of s) {
        // if it is an opening bracket, we push it in to the stack for use later on when we pop it
        if (i in refmap) {
            stack.push(i)
        } 
        // and it is a closing one, we pop the stack, and use the returned opening bracket to find the matching closing brakcet in the refmap
        else if (i !== refmap[stack.pop()]) {
            return false
        };
    }
    // if there is an odd number of characters, there will be some stacks lef
    return stack.length === 0;
};

let gs = '()()(){}{}{}[][][]'
let bs = '()()(){}{}{}[][][}'
console.log(isValid(gs))
console.log(isValid(bs))

// O(N) one pass traverse
// O(N) storing stack for the res is just a boolean
// Are the brackets closed properly?