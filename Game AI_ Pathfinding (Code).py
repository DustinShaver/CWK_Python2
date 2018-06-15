import random
import time
grid = []
#       x, y, distance to destination
dest = [9, 9, 0]
start = ''


# places a random character in the grid
def place_random(c):
    col = random.randint(0, 9)
    row = random.randint(0, 9)
    grid[row][col] = c


# create the initial grid
def create_grid():
    global dest, start
    # start every space as a wall
    for i in range(10):
        grid.append(['#']*10)
    # place random floor tiles
    for i in range(150):
        place_random('.')
    grid[dest[0]][dest[1]] = 'D'


def print_grid():
    for row in grid:
        print("|"+''.join(i for i in row)+"|")


def create_weights():
    # queue used to traverse the grid
    queue = [dest]
    # stack to store the weighted tiles
    stack = []
    while True:
        if len(queue) == 0:
            print("no path found")
            return
        p = queue.pop(0)
        # Start has been found, return the stack
        if grid[p[0]][p[1]] == "S":
            stack.append(p)
            return stack
        # makes sure grid elements which have already been
        # visited and walls are not included in the path
        elif grid[p[0]][p[1]] == 'p' or grid[p[0]][p[1]] == '#':
            continue
        if p[0] < 9:  # add grid square to the right to the queue
            queue.append([p[0]+1, p[1], p[2]+1])
        if p[0] > 0:  # add grid square to the left to the queue
            queue.append([p[0] - 1, p[1], p[2] + 1])
        if p[1] < 9:  # add grid square below to the queue
            queue.append([p[0], p[1]+1, p[2]+1])
        if p[1] > 0:  # add grid square above to the queue
            queue.append([p[0], p[1] - 1, p[2] + 1])
        grid[p[0]][p[1]] = 'p'  # indicate that the square has been visited
        stack.append(p)  # add item to the stack


def create_path(stack):
    # adds the starting tile to the path
    path = [stack.pop()]
    while True:
        # tile to be examined
        n = stack.pop()
        xdist = abs(n[0] - path[-1][0])
        ydist = abs(n[1] - path[-1][1])
        if xdist > 1 or ydist > 1:  # illegal move: square is too far away
            grid[n[0]][n[1]] = '.'
            continue
        if xdist == ydist:  # illegal move: square is a diagonal
            grid[n[0]][n[1]] = '.'
            continue
        if path[-1][2] > n[2]:  # current square is closer to the destination than the last path item
            path.append(n)
            grid[n[0]][n[1]] = '.'
            if n[2] == 0:  # destination reached
                return path
        else:
            grid[n[0]][n[1]] = '.'


def main():
    create_grid()
    print_grid()
    r = int(input("Enter Start row"))
    c = int(input("Enter Start col"))
    grid[r][c] = "S"
    print()
    print_grid()
    s = create_weights()
    if s is not None:
        p = create_path(s)
        for i in range(1, len(p)):
            grid[p[i-1][0]][p[i-1][1]] = '.'
            grid[p[i][0]][p[i][1]] = 'p'
            time.sleep(1)
            print("\n" * 100)
            print_grid()


if __name__ == "__main__":
    main()
