class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(board), len(board[0])
        path = set()
        res = set()
        for word in words:#Put all the words onto a prefix tree
            self.add(word)
        def dfs(word, node, i, j):
            if (i < 0 or j < 0 or i == ROWS or j == COLS or
            (i, j) in path or board[i][j] not in node.children):
                return
            path.add((i, j))
            node = node.children[board[i][j]]
            word = word + board[i][j]
            if node.end:
                res.add(word)

            for dr, dc in directions:
                row = i + dr
                col = j + dc
                dfs(word, node, row, col)
            path.remove((i,j))

        for r in range(ROWS):
            for c in range(COLS):
                dfs("", self.root, r, c)

        return list(res)
