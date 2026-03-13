class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        queue = deque()
        queue.append([1, 0]) # square, moves
        visited = set()


        def intToPos(square):
            y = (square - 1) // length
            x = (square - 1) % length

            if y % 2 == 1:
                x = (length - 1) - x
            
            return (y, x)

        while queue:
            square, moves = queue.popleft()

            for i in range(1, 7): # 1 ~ 6
                nextSquare = square + i

                y, x = intToPos(nextSquare)

                if board[y][x] != -1:
                    nextSquare = board[y][x]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    queue.append((nextSquare, moves + 1))

        return -1
