
import pygame

class Tile:
    def __init__(self, screen, shape, color, initial_offset_x, initial_offset_y, side_length):
        self.screen = screen
        self.shape = shape
        self.color = color
        self.offset_x = initial_offset_x
        self.offset_y = initial_offset_y
        self.side_length = side_length

    def draw_shape(self):
        for point in self.shape:
            column = point[1]
            row = point[0]
            pygame.draw.rect(
                        self.screen,
                        self.color,
                        (column * self.side_length + self.offset_x, row * self.side_length + self.offset_y, self.side_length, self.side_length),
                        0
                    )
        
    def move_shape(self, move_x, move_y):
        self.offset_x = self.offset_x + move_x * self.side_length
        self.offset_y = self.offset_y + move_y * self.side_length

    def return_occupied_tiles(self, matrix, matrix_x_origin, matrix_y_origin):
        return ""