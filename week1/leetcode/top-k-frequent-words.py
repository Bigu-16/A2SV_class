class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        bucket = [[] for _ in range(len(words))]
        ans = []
        for key, val in count.items():
            bucket[val].append(key)
        
        for word in bucket[::-1]:
            if k == 0:
                break
            if len(word) == 0:
                continue
            else:
                word.sort()
                j = 0
                while j < len(word) and k > 0:
                    ans.append(word[j])
                    k -= 1
                    j += 1
        return ans
