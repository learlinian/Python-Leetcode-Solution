class SnakeGame(object):

    def __init__(self, width, height, food):
        self.dots = [[0, 0]]  # head is at the rear of the list
        self.width = width
        self.height = height
        self.food = food

    def move(self, direction):
        new_head = []
        if direction == "R":
            if self.dots[-1][1] == self.width-1:
                return -1
            new_head = [self.dots[-1][0], self.dots[-1][1] + 1]
        elif direction == "L":
            if self.dots[-1][1] == 0:
                return -1
            new_head = [self.dots[-1][0], self.dots[-1][1] - 1]
        elif direction == "D":
            if self.dots[-1][0] == self.height-1:
                return -1
            new_head = [self.dots[-1][0] + 1, self.dots[-1][1]]
        elif direction == "U":
            if self.dots[-1][0] == 0:
                return -1
            new_head = [self.dots[-1][0] - 1, self.dots[-1][1]]

        if not self.food or new_head != self.food[0]:
            del self.dots[0]
            if new_head in self.dots:
                return -1
        else:
            del self.food[0]

        self.dots.append(new_head)
        return len(self.dots) - 1

if __name__ == '__main__':
    obj = SnakeGame(3, 3, [[2,0],[0,0],[0,2],[0,1],[2,2],[0,1]])
    moves = [["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["L"],["D"],["R"],["U"]]
    for m in moves:
        print(obj.move(m[0]))

