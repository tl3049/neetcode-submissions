class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                res = record[-1] + record[-2]
                record.append(res)
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:#integer
                record.append(int(op))
        return sum(record)