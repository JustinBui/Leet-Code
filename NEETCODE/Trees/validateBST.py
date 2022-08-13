class Solution:
    def check(self, root: Optional[TreeNode], choice: str, val_parent: int) -> bool:
        if not root:
            return True
        if choice == 'l' and root.val >= val_parent:
            return False
        elif choice == 'r' and root.val <= val_parent:
            return False

        return self.check(root.left, choice, val_parent) and self.check(root.right, choice, val_parent)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.check(root.left, 'l', root.val) == False or self.check(root.right, 'r', root.val) == False:
            return False

        # If the current node at root is true, keep searching down the tree to see if there are any false
        return self.isValidBST(root.left) and self.isValidBST(root.right)
