class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        res = 0
        for op in operations:
            if op == "+":
                res += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            elif op == "D":
                res += record[-1] * 2
                record.append(record[-1] * 2)
            elif op == "C":
                res -= record.pop()
            else:#integer
                res += int(op)
                record.append(int(op))
        return res