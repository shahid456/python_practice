class Node:
    def __init__(self, info):
        self.data = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)
def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


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
                if temp.data>val:
                    temp=temp.left
                else:
                    temp=temp.right
            if val>temp1.data:
                temp1.right=new_node
            else:
                temp1.left=new_node
            return self.root


def check_binary_search_tree_(root):
    return recur(root)[0]


def recur(root):
    mini = root.data
    maxi = root.data
    if root.left != None:
        if root.data <= root.left.data:
            return False, None, None
        f, fmin, fmax = recur(root.left)
        if not f:
            return False, None, None
        if mini <= fmax:
            return False, None, None
        mini = fmin
    if root.right != None:
        if root.data >= root.right.data:
            return False, None, None
        g, gmin, gmax = recur(root.right)
        if not g:
            return False, None, None
        if maxi >= gmin:
            return False, None, None
        maxi = gmax
    return True, mini, maxi

    g, gmin, gmax = check_binary_search_tree_(root.right)
    return g & f & e, min(mini, fmin, gmin), max(maxi, fmax, gmax)
# Enter you code here.

tree = BinarySearchTree()

t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])
tree.root.left.data=9
inOrder(tree.root)
print(check_binary_search_tree_(tree.root))