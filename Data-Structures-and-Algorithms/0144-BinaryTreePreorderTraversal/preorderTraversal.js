function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

const preorderTraversal = function(root) {
    if (!root) { 
        return [] 
    };
    let stack = [(root)];
    let ans = [];
    while (stack.length) {
        node = stack.pop()
        ans.push(node.val)
        if (node.right) {
            stack.push(node.right)
        }
        if (node.left) {
            stack.push(node.left)
        }
    }
    return ans
};

let root = new TreeNode(0);
let one = new TreeNode(1);
let two = new TreeNode(2);
let three = new TreeNode(3);
root.left = one;
root.right = two;
two.right = three;
console.log(preorderTraversal(root))

// O(N) where N is the total number of nodes
// O(N) for worst case and O(log2(N)) for best case
// Preorder Traversal