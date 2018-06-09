""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return IsBST(root, -1, 10001)
    
def IsBST(node, minleft, maxright):
	if node == None:
		return False	

	if node.left !=  None:
		if node.left.data <= minleft or node.left.data >= node.data:
			return False 	
		
		if IsBST(node.left, minleft, node.data) == False:
			return False

	if node.right !=  None:
		if node.right.data <= node.data or node.right.data >= maxright:
			return False 	
		
		if IsBST(node.right, node.data, maxright) == False:
			return False
	
	return True
    