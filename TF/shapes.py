def generate_shape(shape_id):
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

def get_shape_color(shape_id):
    color = None
    if shape_id == 1:
        color = (255, 255, 0)
    elif shape_id == 2:
        color = (0, 255, 255)
    elif shape_id == 3:
        color = (0, 255, 255)
    elif shape_id == 4:
        color = (255, 128, 0)
    elif shape_id == 5:
        color = (255, 128, 0)
    elif shape_id == 6:
        color = (255, 128, 0)
    elif shape_id == 7:
        color = (255, 128, 0)
    elif shape_id == 8:
        color = (255, 128, 0)
    elif shape_id == 9:
        color = (255, 128, 0)
    elif shape_id == 10:
        color = (255, 128, 0)
    elif shape_id == 11:
        color = (255, 0, 0)
    elif shape_id == 12:
        color = (255, 0, 0)
    elif shape_id == 13:
        color = (128, 0, 255)
    elif shape_id == 14:
        color = (255, 0, 0)
    elif shape_id == 15:
        color = (255, 0, 0)
    elif shape_id == 16:
        color = (255, 0, 0)
    elif shape_id == 17:
        color = (255, 0, 0)
    elif shape_id == 18:
        color = (255, 0, 0)
    elif shape_id == 19:
        color = (255, 0, 0)
    return color
