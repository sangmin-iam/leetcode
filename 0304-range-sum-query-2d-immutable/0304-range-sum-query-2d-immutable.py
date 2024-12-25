class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 1. 0으로 모두 초기화
        self.acc = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
       
        # 4. 나머지 누적합 구하기
        for y in range(1, len(self.acc)):
            for x in range(1, len(self.acc[y])):
                self.acc[y][x] = self.acc[y - 1][x] + self.acc[y][x - 1] - self.acc[y - 1][x - 1] + matrix[y - 1][x - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        # 전체 - 왼쪽 - 위쪽 + 대각선 중복
        whole = self.acc[row2][col2]
        left = self.acc[row2][col1 - 1]
        up = self.acc[row1 - 1][col2]
        duplicate = self.acc[row1 - 1][col1 - 1]

        return whole - left - up + duplicate


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)