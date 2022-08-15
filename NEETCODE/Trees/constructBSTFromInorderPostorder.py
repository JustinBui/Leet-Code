class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            # If our preorder and inorder arrays are null, that means we can return a null, since
            # there are no more subtrees left and right to process. BASE CASE!
            return None

        # The root of the tree is ALWAYS the first value of preorder array
        root = TreeNode(preorder[0])

        # Finding where the first value of preorder locates in inorder
        # (This way, we can determine the left and right subtrees between where mid splits)
        mid = inorder.index(preorder[0])

        # Now that we've determined mid from the line above, we can split preorder and inorder
        # accordingly since we know where each subarray belongs: Left or right of our current root
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
