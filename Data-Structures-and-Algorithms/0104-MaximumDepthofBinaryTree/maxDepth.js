function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
 
const maxDepth = function(root) {
    if (!root) {
        return 0;
    }
    let left = maxDepth(root.left);
    let right = maxDepth(root.right);
    return Math.max(left, right) + 1;
};


let root = new TreeNode(0);
let one = new TreeNode(1);
let two = new TreeNode(2);
let three = new TreeNode(3);
root.left = one;
root.right = two;
two.right = three;
console.log(maxDepth(root))

// O(N) where N is the total number of nodes
// O(N) for worst case and O(log2(N)) for best case
// Max depth of a binary tree