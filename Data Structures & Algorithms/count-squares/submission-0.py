class CountSquares:

    def __init__(self):
        self.pointCounter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointCounter[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for pt in self.points:
            queryX, queryY = pt

            if (pt != point and
                abs(queryX - x) == abs(queryY - y)):

                count += self.pointCounter[(x, queryY)] * self.pointCounter[(queryX, y)]
        return count
                
