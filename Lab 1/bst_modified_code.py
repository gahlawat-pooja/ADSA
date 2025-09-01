import collections
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:           #Corrected to '<'
            node.left = self._insert(node.left, key)
        elif key > node.key:         #Corrected to '>'
            node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)    #earlier it was wrongly calling right subtree for left
        elif key > node.key:
            node.right = self._delete(node.right, key)    #earlier it was wrongly calling left subtree for right
        else:
            if not node.left:     # Corrected to check left child first
                return node.right
            elif not node.right:    # Corrected to check right child second
                return node.left
            temp = self._minValueNode(node.right)     # Corrected to find min in right subtree
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)    # must delete from right subtree
        return node

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def leftRotate(self, key):
        self.root = self._leftRotate(self.root, key)

    def _leftRotate(self, node, key):
        if not node:
            return None
        if key < node.key:   # Rotate left subtree if key is less than node's key 
            node.left = self._leftRotate(node.left, key)
        elif key > node.key:  # Rotate right subtree if key is greater than node's key
            node.right = self._leftRotate(node.right, key)
        else:
            if not node.right:
                return node
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            return new_root
        return node

    def rightRotate(self, key):
        self.root = self._rightRotate(self.root, key)

    def _rightRotate(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._rightRotate(node.left, key)
        elif key > node.key:
            node.right = self._rightRotate(node.right, key)
        else:
            if not node.left:
                return node
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            return new_root
        return node

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(node.key)
            self._inorder(node.right, res)
    def printTree(self):
        self._printTree(self.root, 0)

    def _printTree(self, node, space, indent=5):
        if node is None:
            return
        space += indent
        self._printTree(node.right, space)
        print()
        print(" " * (space - indent) + str(node.key))
        self._printTree(node.left, space)
    
def menu():
    bst = BST()
    while True:
        print("\n--- BST Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Left Rotate")
        print("4. Right Rotate")
        print("5. Inorder Traversal")
        print("6. Print Tree (sideways)")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            key = int(input("Enter key to insert: "))
            bst.insert(key)
        elif choice == '2':
            key = int(input("Enter key to delete: "))
            bst.delete(key)
        elif choice == '3':
            key = int(input("Enter key to left rotate: "))
            bst.leftRotate(key)
        elif choice == '4':
            key = int(input("Enter key to right rotate: "))
            bst.rightRotate(key)
        elif choice == '5':
            print("Inorder:", bst.inorder())
        elif choice == '6':
            print("\nBST Structure:")
            bst.printTree()
        elif choice == '7':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()