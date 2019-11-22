class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, root, target):
        while self.search(root,target) != None:
            if target > root.val:
                root.right = self.delete(root.right, target)
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif  root.val == target:  
                if   root.left is None and root.right is None:
                    root = None
                    return None
                elif root.left is not None and  root.right is None: 
                    a = root.left
                    root = None
                    return a
                elif  root.left is None and  root.right is not None:      
                    a = root.right
                    root = None
                    return a
                elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val
                    root.left = self.delete(root.left, a.val)          
        return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
    def modify(self, root, target, new_val):
        if target == new_val:
            return root
        else: 
            k=0                                          
            a=self.search(root,target)
            if a==None:
                return root    
            else:
                while a != None and a.val == target:
                    k=k+1
                    a=a.left  
                self.delete(root,target)
                while k>0:
                    self.insert(root,new_val)
                    k=k-1
                return root 
