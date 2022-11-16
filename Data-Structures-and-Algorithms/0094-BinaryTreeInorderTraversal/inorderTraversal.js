function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

function inorderTraversal(root) {
    const stack = [];
    const res = [];
    while (root || stack.length) {
        // go left, stack each node on the way, until I encounter null after a leaf
        if (root) {
            stack.push(root)
            root = root.left
        }
        // when I encounter a null, I want to go back to the leaf and record the leaf value, which is in the stack already
        if (!root) {
            root = stack.pop()
            res.push(root.val)
            // then we check the right side, if exist, we stack it, if not, we pop another stack through the first if statement
            root = root.right
        }
    }
    return res
}

let root = new TreeNode(0);
let one = new TreeNode(1);
let two = new TreeNode(2);
let three = new TreeNode(3);
root.left = one;
root.right = two;
two.right = three;
console.log(inorderTraversal(root))

// O(N) where N is the total number of nodes
// O(N) for worst case and O(log2(N)) for best case
// Inorder Traversal