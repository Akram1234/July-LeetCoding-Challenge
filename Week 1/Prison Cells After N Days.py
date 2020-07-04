class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def findNext(pre):
            return [0]+[pre[j-1]^pre[j+1]^1 for j in range(1,7)]+[0]
            
        cycle = []
        state = findNext(cells)
        while state not in cycle:
            cycle.append(state)
            state = findNext(state)
        return cycle[(N - 1)%len(cycle)]
