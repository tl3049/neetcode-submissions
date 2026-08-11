from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dic = Counter(students)
        count = 0
        for s in sandwiches:
            if dic[s] > 0:
                dic[s] -= 1
                count += 1
            else:
                break
        return len(students) - count