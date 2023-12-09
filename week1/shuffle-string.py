class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapped = dict(zip(indices, s))
        sorted_mapped = ''.join(mapped[i] for i in sorted(mapped.keys()))
        
        return sorted_mapped
        