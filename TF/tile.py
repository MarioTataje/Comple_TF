
import pygame

class Tile:
    def __init__(self, screen, shape, color, initial_offset_x, initial_offset_y, side_length, number):
        self.screen = screen
        self.tile_number = number
        self.shape = shape
        self.color = color
        self.offset_x = initial_offset_x
        self.offset_y = initial_offset_y
        self.side_length = side_length

    def draw_shape(self):
        border = 2;

        for point in self.shape:
            column = point[1]
            row = point[0]
            pygame.draw.rect(
                        self.screen,
                        self.color,
                        (column * self.side_length + self.offset_x, row * self.side_length + self.offset_y, self.side_length, self.side_length),
                        0
                    )
            pygame.draw.rect(
                        self.screen,
                        (0,0,0),
                        (column * self.side_length + self.offset_x, row * self.side_length + self.offset_y, self.side_length, self.side_length),
                        1
                    )

        
    def move_shape(self, move_x, move_y):
        self.offset_x = self.offset_x + move_x * self.side_length
        self.offset_y = self.offset_y + move_y * self.side_length

    #devolvemos [[x,y],...]
    def return_occupied_tiles(self, matrix_x_origin, matrix_y_origin):
        points = []
        border = 2;

        offset_x_tiles = self.offset_x / self.side_length;
        offset_y_tiles = self.offset_y / self.side_length;

        for point in self.shape:
            column = point[1]
            row = point[0]
            x = (column + offset_x_tiles) - matrix_x_origin
            y = (row + offset_y_tiles) - matrix_y_origin
            points.append([x,y])

        return points

    def get_tile_number(self):
        return self.tile_number;