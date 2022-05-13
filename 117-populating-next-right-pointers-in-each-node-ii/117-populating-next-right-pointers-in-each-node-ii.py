class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            temp = Node()
            prev = temp
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            curr = temp.next
        return root