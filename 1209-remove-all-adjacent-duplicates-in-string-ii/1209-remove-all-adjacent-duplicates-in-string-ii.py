class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        co = []
        for i in s:
            if st and st[-1] == i:
                st.append(i)
                co.append(co[-1] + 1)
            else:
                st.append(i)
                co.append(1)
            if co and co[-1] == k:
                while co[-1]!=1:
                    co.pop()
                    st.pop()
                co.pop()
                st.pop()

        return "".join(st)