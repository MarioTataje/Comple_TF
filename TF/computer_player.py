from random import randint
from copy import deepcopy

def Tetris(target, limit_tetris):
    available_target = AvailableTarget(target)
    available_list = AvailableList(limit_tetris)
    solution_list = TetrisDFS(
        available_target.clone_remain_target(),
        available_list.clone_remain_list())
    return generate_solution(solution_list, available_target.get_num_row(), #modify the solution into the required format (ie: [shape_id,order put on target])
                             available_target.get_num_column())

#use DEPTH FIRST SEARCH if there are 15 pieces of tetris or less (faster + 100% accuracy)
def TetrisDFS(target, limit_tetris): #append tarm id of shape
    # set initial values
    count_pieces = 0
    for i in limit_tetris:
        count_pieces += limit_tetris[i]
    # so that we can refer to it when ja hai remove from target
    solve_order = [[0, -1, -1] for i in range(count_pieces)]
    temp_index = 0  # refer to current index as going through loop
    for i in limit_tetris:
        for j in range(limit_tetris[i]):
            solve_order[temp_index][0] = i
            temp_index += 1
    for i in range(len(solve_order)):
        available_row = -1
        available_column = -1
        while available_row == -1:
            (available_row, available_column) = get_position(
                solve_order[i], target)
            if available_row != -1:
                solve_order[i][1] = available_row
                solve_order[i][2] = available_column
                place(i, solve_order, target)
            else:
                please_move(i-1, solve_order, target)

    return solve_order

#service function for Depth first search
def get_next_location(now_row, now_column, target):
    if now_row == -1:
        return(0, 0)
    else:
        next_row = now_row
        next_column = now_column+1
        if next_column >= len(target[0]):
            next_column = 0
            next_row += 1
        if next_row >= len(target):
            return (-1, -1)
        else:
            return (next_row, next_column)


def can_place(shape_id, row_num, col_num, target):
    # check id can plae in target at row,column
    if target[row_num][col_num] != 1:
        return False
    else:
        shape = get_shape_array(shape_id)
        for i in range(4):
            # check shape whether it is possible to place at some position
            if (row_num + shape[i][0] < 0 or
                    row_num + shape[i][0] >= len(target) or
                    col_num + shape[i][1] < 0 or
                    col_num+shape[i][1] >= len(target[0]) or
                    target[row_num + shape[i][0]][col_num+shape[i][1]] != 1):
                return False
        else:
            return True


def get_position(solve_piece_info, target):
    next_row = 0
    next_column = 0
    num_round = -1
    while next_row != -1:
        num_round += 1
        if num_round == 0:
            (next_row, next_column) = get_next_location(
                solve_piece_info[1], solve_piece_info[2], target)
        else:
            (next_row, next_column) = get_next_location(
                next_row, next_column, target)
        if next_row != -1:
            result = can_place(
                solve_piece_info[0], next_row, next_column, target)
            if result:
                return (next_row, next_column)
    else:
        return (-1, -1)


def please_move(index, solve_order, target):
    # move testris piece at index on target until can place at new position
    shape = get_shape_array(solve_order[index][0])
    for i in range(4):
        target[solve_order[index][1] + shape[i][0]
               ][solve_order[index][2] + shape[i][1]] = 1

    moved = False
    while not moved:
        (next_row, next_column) = get_next_location(
            solve_order[index][1], solve_order[index][2], target)
        while next_row != -1:
            if can_place(solve_order[index][0], next_row, next_column, target):
                solve_order[index][1] = next_row
                solve_order[index][2] = next_column
                place(index, solve_order, target)
                moved = True
                break
            else:
                (next_row, next_column) = get_next_location(
                    next_row, next_column, target)
        else:
            solve_order[index][1] = -1
            solve_order[index][2] = -1
            please_move(index-1, solve_order, target)


def place(index, solve_oder, target):
    shape = get_shape_array(solve_oder[index][0])
    for i in range(4):
        target[solve_oder[index][1]+shape[i][0]
               ][solve_oder[index][2] + shape[i][1]] = 0


#class as service function for Random search:
class AvailableTarget:
    def __init__(self, target):
        self._target = target
        self._max_width = len(target)
        self._max_height = len(target[0])
        self._solution = []
        self._available_position = [(x, y) for x in range(self._max_height)
                                    for y in range(self._max_width)
                                    if target[x][y] != 0]
        self._available_len = len(self._available_position)
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= self._available_len:
            self._current_index = 0
            raise StopIteration
        else:
            self._current_index += 1
            return self._available_position[self._current_index-1]

    def get_num_column(self):
        return self._max_width

    def get_num_row(self):
        return self._max_height

    def remain_position(self):
        return self._available_len

    def update(self):
        self._available_position = [(x, y) for x in range(self._max_height)
                                    for y in range(self._max_width)
                                    if self._available_target[x][y] != 0]
        self._available_len = len(self._available_position)

    def clone_remain_target(self):
        return deepcopy(self._target)

    def can_place(self, shape_id, x, y):
        shape = get_shape_array(shape_id)
        # check shape whether it is possible to place at some position
        # and do not exceeds target size
        for i in range(4):
            if (x + shape[i][0] < 0 or x + shape[i][0] >= self.get_num_column() or
                y + shape[i][1] < 0 or y + shape[i][1] >= self.get_num_row() or
                    self._target[x + shape[i][0]][y+shape[i][1]] != 1):
                return False
        else:
            return True

    def place(self, shape_id, x, y):
        self._solution.append([shape_id, x, y])
        shape = get_shape_array(shape_id)
        for i in range(4):
            self._target[x + shape[i][0]][y+shape[i][1]] = 0

    def get_solution(self):
        return self._solution


class AvailableList: #only check through the target that is 1(faster as doesn't run through 0)
    def __init__(self, limit_tetris):
        self._limit_list = limit_tetris
        self._available_list = []
        self._list_len = 0
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= self._list_len:
            self._current_index = 0
            raise StopIteration
        else:
            self._current_index += 1  # if there is still shapes in tetris list
            return self._available_list[self._current_index-1]

    def prompt(self, option=0):  # random by using forward method if option = 0
        # return only the shape_id that is available in the tetris list (doesn't look at 0)
        self._available_list = [
            key for key in self._limit_list if self._limit_list[key] != 0]
        self._list_len = len(self._available_list)
        self._current_index = 0
        if option >= 2:  # if option = 2, the list generated will be in random
            for i in range(self._list_len):
                j = randint(0, self._list_len-1)
                temp = self._available_list[i]
                self._available_list[i] = self._available_list[j]
                self._available_list[j] = temp
        # if option = 1, list generated will be in backward order
        elif option == 1:
            self._available_list.reverse()

    def used(self, shape_id):
        self._limit_list[shape_id] -= 1

    def remain_pieces(self):
        return sum(self._limit_list.values())

    def can_use(self, shape_id):
        return self._limit_list[shape_id] > 0

    def clone_remain_list(self):
        return deepcopy(self._limit_list)
     
    
#general functions for BOTH random and depth first search:
def generate_solution(solutions, num_target_row, num_target_column):
    solution = [[(0, 0) for col in range(0, num_target_column)]
                for row in range(0, num_target_row)]
    for i in range(len(solutions)):
        [shape_id, x, y] = solutions[i]
        shape=get_shape_array(shape_id)
        for j in range(4):
            solution[x + shape[j][0]][y+shape[j][1]] = (shape_id, i+1) 
    return solution


def get_shape_array(shape_id): 
    shape = None
    if shape_id == 1:
        shape = [[0, 0], [0, 1], [1, 0], [1, 1]]
    elif shape_id == 2:
        shape = [[0, 0], [1, 0], [2, 0], [3, 0]]
    elif shape_id == 3:
        shape = [[0, 0], [0, 1], [0, 2], [0, 3]]
    elif shape_id == 4:
        shape = [[0, 0], [1, 0], [2, 0], [2, 1]]
    elif shape_id == 5:
        shape = [[0, 0], [1, -2], [1, -1], [1, 0]]
    elif shape_id == 6:
        shape = [[0, 0], [0, 1], [1, 1], [2, 1]]
    elif shape_id == 7:
        shape = [[0, 0], [0, 1], [0, 2], [1, 0]]
    elif shape_id == 8:
        shape = [[0, 0], [1, 0], [2, -1], [2, 0]]
    elif shape_id == 9:
        shape = [[0, 0], [0, 1], [0, 2], [1, 2]]
    elif shape_id == 10:
        shape = [[0, 0], [0, 1], [1, 0], [2, 0]]
    elif shape_id == 11:
        shape = [[0, 0], [1, 0], [1, 1], [1, 2]]
    elif shape_id == 12:
        shape = [[0, 0], [1, 0], [1, 1], [2, 0]]
    elif shape_id == 13:
        shape = [[0, 0], [1, -1], [1, 0], [1, 1]]
    elif shape_id == 14:
        shape = [[0, 0], [1, -1], [1, 0], [2, 0]]
    elif shape_id == 15:
        shape = [[0, 0], [0, 1], [0, 2], [1, 1]]
    elif shape_id == 16:
        shape = [[0, 0], [0, 1], [1, -1], [1, 0]]
    elif shape_id == 17:
        shape = [[0, 0], [1, 0], [1, 1], [2, 1]]
    elif shape_id == 18:
        shape = [[0, 0], [0, 1], [1, 1], [1, 2]]
    elif shape_id == 19:
        shape = [[0, 0], [1, -1], [1, 0], [2, -1]]
    return shape

