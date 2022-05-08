# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def _to_stack(self, nlist):
        answer = []
        for i in nlist:
            if i.isInteger():
                answer.append(i.getInteger())
            else:
                answer.extend(self._to_stack(i.getList()))
        return answer
        
    def __init__(self, nestedList: [NestedInteger]):
        self.nlist = self._to_stack(nestedList)
    
    def next(self) -> int:
        return self.nlist.pop(0)
    
    def hasNext(self) -> bool:
        if self.nlist:
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())