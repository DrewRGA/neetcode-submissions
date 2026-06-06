# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        temp_list = []
        result = []

        for i in range(len(pairs)):

            j = i

            while j > 0 and pairs[j].key < pairs[j-1].key:
                #print([(p.key, p.value) for p in pairs])
                temp_list = pairs[j-1]
                pairs[j-1] = pairs[j]
                pairs[j] = temp_list
                j -= 1

            result.append(pairs.copy())

        return result