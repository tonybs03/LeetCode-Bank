function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

const postorderTraversal = function(root) {
    let ans = [];
    const poT = (node) => {
        if (node) {
            poT(node.left)
            poT(node.right)
            ans.push(node.val)
        }
    }

    poT(root);
    return ans
};

let root = new TreeNode(0);
let one = new TreeNode(1);
let two = new TreeNode(2);
let three = new TreeNode(3);
root.left = one;
root.right = two;
two.right = three;
console.log(postorderTraversal(root))

// O(N) where N is the total number of nodes
// O(N) for worst case and O(log2(N)) for best case
// Postorder Traversal