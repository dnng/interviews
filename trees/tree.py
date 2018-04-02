#/usr/bin/env python3
""" A basic Binary Tree class"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root:
            self._add(val, self.root)
        else:
            self.root = Node(val)

    def _add(self, val, node):
        if node.val > val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        elif node.val < val:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if node.val == val:
            return node
        elif node.val > val:
            return self._find(val, node.left)
        elif node.val < val:
            return self._find(val, node.right)

    def delete(self):
        self.root = None

    def print_inorder(self):
        if self.root:
            self._print_inorder(self.root)
        print('')

    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(str(node.val) + ' ', end='')
            self._print_inorder(node.right)

    def print_preorder(self):
        if self.root:
            self._print_preorder(self.root)
        print('')

    def _print_preorder(self, node):
        if node:
            print(str(node.val) + ' ', end='')
            self._print_preorder(node.left)
            self._print_preorder(node.right)

    def print_postorder(self):
        if self.root:
            self._print_postorder(self.root)
        print('')

    def _print_postorder(self, node):
        if node:
            self._print_postorder(node.left)
            self._print_postorder(node.right)
            print(str(node.val) + ' ', end='')

    def height(self):
        # Height as a function compares two subtrees and returns the biggest one
        # at each step
        return self._height(self.root)

    def _height(self, node):
        if node:
            l_height = self._height(node.left)
            r_height = self._height(node.right)

            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1
        else:
            return 0

    def print_level_order(self):
        if self.root:
            # h = self.height()
            # for i in range(1, h+1):
            #     self._print_level_order(self.root, i)
            q = [self.root]
            while q:
                aux = q.pop(0)
                print(str(aux.val) + ' ', end='')
                if aux.left:
                    q.append(aux.left)
                if aux.right:
                    q.append(aux.right)
        print("")

    def _print_level_order(self, node, level):
        if node:
            if level == 1:
                print(str(node.val) + ' ', end='')
            else:
                self._print_level_order(node.left, level-1)
                self._print_level_order(node.right, level-1)
        else:
            return None

tree = Tree()
for i in (5,3,8,2,4,7,9,1,6,10):
    tree.add(i)

tree.print_inorder()
tree.print_preorder()
tree.print_postorder()
print(tree.height())
tree.print_level_order()
# three = tree.find(3)
# print(three.val)
# print(three.left.val)
# print(three.right.val)
# tree.delete()