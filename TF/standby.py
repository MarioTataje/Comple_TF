import pygame
import shapes
import asyncio
import random
import time
import computer_player
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_SPACE
)
from dice import Dice
from tile import Tile


class Standby:
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.tittle = pygame.display.set_caption("Standby")
        self.image = pygame.image.load("Standby.png")
        self.scaledImage = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        self.gray = (128, 128, 128)
        self.newGray = (55, 118, 118)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.Verify = False
        self.round = 0
        self.roundText = 'Ronda : '
        self.count = 11
        self.myFont = pygame.font.SysFont('comicsans', 30)
        self.roundFont = self.myFont.render(str(self.round), 1, self.white)
        self.roundTextFont = self.myFont.render(self.roundText, 1, self.white)
        self.countFont = self.myFont.render(str(self.count), 1, self.white)
        self.VerifyDice = False
        self.clock = pygame.time.Clock()
        self.side_length = 40
        self.diceImage = 0
        self.n = 0
        self.playing = True
        self.player_tiles = []
        self.computer_tiles = []
        self.selected_tile_index = 0
        self.computer_thinking = False
        self.computer_found_solution = False
        self.solution = None;

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.white)
        return textSurface, textSurface.get_rect()

    def button(self, x, y, width, height, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, self.black, ((x - 10) - 2, (y - 10) - 2, (width + 20) + 4, (height + 20) + 4),
                             0)
            pygame.draw.rect(self.screen, self.newGray, (x - 10, y - 10, width + 20, height + 20))
            word = pygame.font.SysFont('comicsans', 30)

            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.screen, self.black, (x - 2, y - 2, width + 4, height + 4), 0)
            pygame.draw.rect(self.screen, self.gray, (x, y, width, height))
            word = pygame.font.SysFont('comicsans', 25)

        textSurf, textRect = self.text_objects(text, word)
        textRect.center = ((x + int((width / 2))), (y + int((height / 2))))
        self.screen.blit(textSurf, textRect)

    def throwDice(self):
        dice = Dice()
        self.n = dice.drawDice()
        self.Verify = True
        self.diceImage = dice.dice
        self.VerifyDice = True

    def drawGrid(self, matrix, offsetX, offsetY):
        sideLength = 40
        row = 0
        column = 0

        pygame.draw.rect(
            self.screen,
            self.white,
            (column * sideLength + offsetX, row * sideLength + offsetY, sideLength * len(matrix[0]),
             sideLength * len(matrix)),
            0
        )

        for matrixRow in matrix:
            for element in matrixRow:
                if element != 0:
                    pygame.draw.rect(
                        self.screen,
                        self.gray,
                        (column * sideLength + offsetX, row * sideLength + offsetY, sideLength, sideLength),
                        2
                    )
                column = column + 1
            column = 0
            row = row + 1

    def solve_puzzle(self):
        print('hola')
        matrix = [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1]
        ]

        sleepTime = random.randint(10, 30)
        print('Sleeping for: ' + str(sleepTime));
        time.sleep(sleepTime)

        limit_tetris = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 0, 10: 0, 11: 0, 12: 0, 13: 1, 14: 0, 15: 0,
                        16: 0, 17: 0, 18: 1, 19: 0}

        self.solution = computer_player.Tetris(matrix, limit_tetris);
        self.computer_found_solution = True;

    def fire_and_forget(self, task, *args, **kwargs):
        loop = asyncio.get_event_loop()
        if callable(task):
            return loop.run_in_executor(None, task, *args, **kwargs)
        else:
            raise TypeError('Task must be a callable')

    def run(self, _running):
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        while _running:
            self.screen.blit(self.scaledImage, (0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if self.playing:
                        selected_tile = self.player_tiles[self.selected_tile_index]
                        if event.key == K_UP:
                            selected_tile.move_shape(0, -1);
                        if event.key == K_DOWN:
                            selected_tile.move_shape(0, 1);
                        if event.key == K_LEFT:
                            selected_tile.move_shape(-1, 0);
                        if event.key == K_RIGHT:
                            selected_tile.move_shape(1, 0);
                        if event.key == K_SPACE:
                            self.selected_tile_index = self.selected_tile_index + 1;
                            if self.selected_tile_index == len(self.player_tiles):
                                self.selected_tile_index = 0;
                if event.type == pygame.USEREVENT:
                    if self.VerifyDice:
                        self.count -= 1
                        self.countFont = self.myFont.render(str(self.count), 1, self.white)
                        if self.count == -1:
                            self.count = 11
                            self.VerifyDice = False
                            self.round += 1
                            self.roundFont = self.myFont.render(str(self.round), 1, self.white)

            self.button((self.screen_width * 0.5) - 50, 20, 100, 40, 'Tirar', self.throwDice)

            matrix = [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1]
            ]

            grid_origin_player_x = 1
            grid_origin_player_y = 4
            grid_origin_computer_x = 17
            grid_origin_computer_y = 4

            self.drawGrid(matrix, grid_origin_player_x * self.side_length, grid_origin_player_y * self.side_length)
            self.drawGrid(matrix, grid_origin_computer_x * self.side_length, grid_origin_computer_y * self.side_length)

            limit_tetris = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 0, 10: 0, 11: 0, 12: 0, 13: 1, 14: 0,
                            15: 0, 16: 0, 17: 0, 18: 1, 19: 0}

            if len(self.player_tiles) == 0:
                shape_offset_x = grid_origin_player_x * self.side_length
                distance_shape = 4 * self.side_length
                for key, value in limit_tetris.items():
                    if value != 0:
                        shape = shapes.generate_shape(key);
                        # get color from shape colors
                        new_tile = Tile(self.screen, shape, self.green, shape_offset_x,
                                        (grid_origin_player_y + 10) * self.side_length, self.side_length)
                        new_tile.draw_shape();
                        shape_offset_x = shape_offset_x + distance_shape
                        self.player_tiles.append(new_tile);
            else:
                for tile in self.player_tiles:
                    tile.draw_shape();

            if not self.computer_found_solution:
                shape_offset_x = grid_origin_computer_x * self.side_length
                distance_shape = 4 * self.side_length
                for key, value in limit_tetris.items():
                    if value != 0:
                        shape = shapes.generate_shape(key);
                        # get color from shape colors
                        new_tile = Tile(self.screen, shape, self.red, shape_offset_x,
                                        (grid_origin_player_y + 10) * self.side_length, self.side_length)
                        new_tile.draw_shape();
                        shape_offset_x = shape_offset_x + distance_shape
            else:
                offsetX = self.side_length * grid_origin_computer_x;
                offsetY = self.side_length * grid_origin_computer_y;
                row = 0
                column = 0

                for solution_row in self.solution:
                    for solution_column in solution_row:
                        if solution_column[0] != 0:
                            pygame.draw.rect(
                                self.screen,
                                self.blue,
                                (
                                column * self.side_length + offsetX, row * self.side_length + offsetY, self.side_length,
                                self.side_length),
                                0
                            )
                        column = column + 1;
                    column = 0
                    row = row + 1;

            if not self.computer_thinking and not self.computer_found_solution:
                self.computer_thinking = True;
                self.fire_and_forget(self.solve_puzzle);

            if self.Verify:
                self.screen.blit(self.diceImage, ((self.screen_width * 0.50) - 35, self.screen_height * 0.15))
            if self.VerifyDice:
                self.screen.blit(self.countFont, (1000, 35))
            self.screen.blit(self.roundTextFont, (1100, 35))
            self.screen.blit(self.roundFont, (1200, 35))
            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()
        quit()
