class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        candidates.sort()
        def backtrack(val, curr, index): 
            if val == 0:
                final.append(curr)
                return 
            
            if val < 0: 
                return 

            for i in range(index, len(candidates)): 
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                backtrack(val - candidates[i], curr + [candidates[i]], i + 1)

        backtrack(target, [], 0)
        return final