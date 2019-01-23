class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)
def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.info,end=" ")
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        temp=self.root
        new_node=Node(val)
        temp=self.root
        if temp==None:
            self.root=new_node
            return self.root
        else:

            while temp!=None:
                temp1=temp
                if temp.info>val:
                    temp=temp.left
                else:
                    temp=temp.right
            if val>temp1.info:
                temp1.right=new_node
            else:
                temp1.left=new_node
            return self.root


# Enter you code here.

tree = BinarySearchTree()

t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])
inOrder(tree.root)
preOrder(tree.root)
postOrder(tree.root)
