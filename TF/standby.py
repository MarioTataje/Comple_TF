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

import utils
from dice import Dice
from tile import Tile
from win import Win
from lose import Lose


def WinGame():
    screen_dimensions = utils.get_screen_dimensions()
    winPlayer = Win(screen_dimensions['width'], screen_dimensions['height'])
    winPlayer.run(True)


def LoseGame():
    screen_dimensions = utils.get_screen_dimensions()
    losePlayer = Lose(screen_dimensions['width'], screen_dimensions['height'])
    losePlayer.run(True)


class Standby:
    def __init__(self, width, height, target, pieces):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.target = target
        self.pieces = pieces
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.tittle = pygame.display.set_caption("Standby")
        self.image = pygame.image.load("assets/Standby.png")
        self.scaledImage = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        self.gray = (128, 128, 128)
        self.newGray = (55, 118, 118)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.Verify = False
        self.VerifyDice = False
        self.VerifyPlayerWin = False
        self.VerifyMachineWin = False
        self.round = 0
        self.count = 31
        self.playerScore = 0
        self.machineScore = 0
        self.roundText = 'Ronda : '
        self.playerScoreText = 'Puntaje Jugador : '
        self.machineScoreText = 'Puntaje Maquina : '
        self.myFont = pygame.font.SysFont('comicsans', 30)
        self.countFont = self.myFont.render(str(self.count), 1, self.white)
        self.roundFont = self.myFont.render(str(self.round), 1, self.white)
        self.roundTextFont = self.myFont.render(self.roundText, 1, self.white)
        self.playerScoreFont = self.myFont.render(str(self.playerScore), 1, self.white)
        self.playerScoreTextFont = self.myFont.render(self.playerScoreText, 1, self.white)
        self.machineScoreFont = self.myFont.render(str(self.machineScore), 1, self.white)
        self.machineScoreTextFont = self.myFont.render(self.machineScoreText, 1, self.white)
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
        self.computer_won = False
        self.grid_origin_computer_x = 17
        self.grid_origin_computer_y = 4
        self.solution = None;
        self.there_is_winner = False;

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

    def winPointPlayer(self):
        self.VerifyPlayerWin = True

    def winPointMachine(self):
        self.VerifyMachineWin = True

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
        self.solution = computer_player.Tetris(self.target, self.pieces)

        sleepTime = random.randint(2, 5)
        print('Sleeping for: ' + str(sleepTime))
        time.sleep(sleepTime)

        print('Found solution')
        self.computer_found_solution = True
        self.computer_move_tiles()

    def create_empty_solution(self):
        empty_solution = []

        for row in self.target:
            new_row = []
            for column in row:
                new_row.append(0)
            empty_solution.append(new_row)

        return empty_solution

    def computer_move_tiles(self):
        if self.computer_won:
            return

        time.sleep(0.5)

        row = 0
        column = 0

        shapes_moved = []

        for solution_row in self.solution:
            for solution_column in solution_row:
                shape_id = solution_column[0]
                if shape_id != 0 and not shape_id in shapes_moved:
                    for tile in self.computer_tiles:
                        tile_number = tile.get_tile_number()
                        if tile_number == shape_id:
                            shapes_moved.append(shape_id)
                            occupied_tiles = tile.return_occupied_tiles(self.grid_origin_computer_x,
                                                                        self.grid_origin_computer_y)
                            current_left_top = occupied_tiles[0]
                            current_smallest_y = current_left_top[1]
                            current_smallest_x = current_left_top[0]

                            for point in occupied_tiles:
                                if point[1] < current_smallest_y:
                                    current_left_top = point
                                    current_smallest_y = current_left_top[1]
                                    current_smallest_x = current_left_top[0]
                                else:
                                    if point[1] == current_smallest_y:
                                        if point[0] < current_smallest_x:
                                            current_left_top = point
                                            current_smallest_y = current_left_top[1]
                                            current_smallest_x = current_left_top[0]

                            if current_left_top[1] > row:
                                tile.move_shape(0, -1)
                                self.computer_move_tiles()
                                return

                            if current_left_top[0] > column:
                                tile.move_shape(-1, 0)
                                self.computer_move_tiles()
                                return

                            if current_left_top[0] < column:
                                tile.move_shape(1, 0)
                                self.computer_move_tiles()
                                return

                column = column + 1
            column = 0
            row = row + 1

    def check_won(self, current_tiles, origin_x, origin_y):
        # no podemos verificar quien gano hasta que tengamos solucion
        if self.solution is None:
            return False

        current_solution = self.create_empty_solution()

        for tile in current_tiles:
            occupied_tiles = tile.return_occupied_tiles(origin_x, origin_y)
            tile_number = tile.get_tile_number()
            for occupied in occupied_tiles:
                x = int(occupied[0])
                y = int(occupied[1])
                if x >= len(self.target[0]) or x < 0:
                    return False

                if y >= len(self.target) or y < 0:
                    return False

                current_solution[y][x] = tile_number

        row = 0
        column = 0

        for solution_row in self.solution:
            for solution_column in solution_row:
                matching_shape_id = current_solution[row][column]
                if matching_shape_id != solution_column[0]:
                    return False
                column = column + 1
            column = 0
            row = row + 1

        return True

    def fire_and_forget(self, task, *args, **kwargs):
        loop = asyncio.get_event_loop()
        if callable(task):
            return loop.run_in_executor(None, task, *args, **kwargs)
        else:
            raise TypeError('Task must be a callable')

    def start_round(self):
        grid_origin_player_x = 1
        grid_origin_player_y = 4

        self.drawGrid(self.target, grid_origin_player_x * self.side_length, grid_origin_player_y * self.side_length)
        self.drawGrid(self.target, self.grid_origin_computer_x * self.side_length,
                      self.grid_origin_computer_y * self.side_length)

        if len(self.player_tiles) == 0:
            shape_offset_x = grid_origin_player_x * self.side_length
            distance_shape = 4 * self.side_length
            for key, value in self.pieces.items():
                if value != 0:
                    shape = shapes.generate_shape(key)
                    color = shapes.get_shape_color(key)
                    new_tile = Tile(self.screen, shape, color, shape_offset_x,
                                    (grid_origin_player_y + 10) * self.side_length, self.side_length, key)
                    new_tile.draw_shape()
                    shape_offset_x = shape_offset_x + distance_shape
                    self.player_tiles.append(new_tile)
        else:
            for tile in self.player_tiles:
                tile.draw_shape()

        if len(self.computer_tiles) == 0:
            shape_offset_x = self.grid_origin_computer_x * self.side_length
            distance_shape = 4 * self.side_length
            for key, value in self.pieces.items():
                if value != 0:
                    shape = shapes.generate_shape(key)
                    color = shapes.get_shape_color(key)
                    new_tile = Tile(self.screen, shape, color, shape_offset_x,
                                    (grid_origin_player_y + 10) * self.side_length, self.side_length, key)
                    new_tile.draw_shape()
                    shape_offset_x = shape_offset_x + distance_shape
                    self.computer_tiles.append(new_tile)
        else:
            for tile in self.computer_tiles:
                tile.draw_shape()

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
                            selected_tile.move_shape(0, -1)
                        if event.key == K_DOWN:
                            selected_tile.move_shape(0, 1)
                        if event.key == K_LEFT:
                            selected_tile.move_shape(-1, 0)
                        if event.key == K_RIGHT:
                            selected_tile.move_shape(1, 0)
                        if event.key == K_SPACE:
                            self.selected_tile_index = self.selected_tile_index + 1
                            if self.selected_tile_index == len(self.player_tiles):
                                self.selected_tile_index = 0
                if event.type == pygame.USEREVENT:
                    if self.VerifyDice:
                        self.count -= 1
                        self.countFont = self.myFont.render(str(self.count), 1, self.white)
                        if self.count == -1:
                            self.count = 31
                            self.VerifyDice = False
                            self.round += 1
                            self.roundFont = self.myFont.render(str(self.round), 1, self.white)
                    if self.VerifyPlayerWin:
                        self.playerScore += 1
                        self.playerScoreFont = self.myFont.render(str(self.playerScore), 1, self.white)
                        self.VerifyPlayerWin = False
                    if self.VerifyMachineWin:
                        self.machineScore += 1
                        self.machineScoreFont = self.myFont.render(str(self.machineScore), 1, self.white)
                        self.computer_won = False
                        self.VerifyMachineWin = False
                    if self.count == 31:
                        self.computer_thinking = False
                        self.computer_found_solution = False
                        self.there_is_winner = False

            self.button((self.screen_width * 0.5) - 50, 20, 100, 40, 'Tirar', self.throwDice)
            #self.button(50, 20, 100, 40, 'Gane', self.winPointPlayer)

            grid_origin_player_x = 1
            grid_origin_player_y = 4

            if self.count < 31:
                self.start_round()

            if self.count == 31:
                self.player_tiles = []
                self.computer_tiles = []

            if not self.computer_thinking and not self.computer_found_solution:
                self.computer_thinking = True;
                self.fire_and_forget(self.solve_puzzle);

            # Check if won
            if not self.there_is_winner:
                if self.check_won(self.player_tiles, grid_origin_player_x, grid_origin_player_y):
                    self.there_is_winner = True
                    self.VerifyPlayerWin = True
                    print('Player won')

                if self.check_won(self.computer_tiles, self.grid_origin_computer_x, self.grid_origin_computer_y):
                    self.there_is_winner = True
                    self.VerifyMachineWin = True
                    print('Computer won')

            if self.Verify:
                self.screen.blit(self.diceImage, ((self.screen_width * 0.50) - 35, self.screen_height * 0.15))
            if self.VerifyDice:
                self.screen.blit(self.countFont, (1000, 35))
            self.screen.blit(self.roundTextFont, (1100, 35))
            self.screen.blit(self.roundFont, (1200, 35))
            self.screen.blit(self.playerScoreTextFont, (50, 100))
            self.playerScoreTextFont = self.myFont.render(self.playerScoreText, 1, self.white)
            self.screen.blit(self.playerScoreFont, (250, 100))
            self.screen.blit(self.machineScoreTextFont, (800, 100))
            self.screen.blit(self.machineScoreFont, (1000, 100))
            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()
        quit()
