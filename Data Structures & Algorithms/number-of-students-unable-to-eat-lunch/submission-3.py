class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        n_squ = sum(students)
        n_cir = n - n_squ
        count = 0
        for i in range(n):
            if sandwiches[i] == 0:
                n_cir -= 1
            else:
                n_squ -= 1
            if n_cir < 0 or n_squ < 0:
                break
            else:
                count += 1
        return n - count
