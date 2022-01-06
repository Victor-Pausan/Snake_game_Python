import pygame
import random
import time

'''
colors = {
    'dark green' : (60,99,40),
    'green' : (82,135,55)
}
'''

size = 64

class Fruit:
    def __init__(self, parent_screen):
        self.x = random.randint(64, 896) // 64 * 64
        self.y = random.randint(64, 640) // 64 * 64
        self.image = pygame.image.load('Images/apple.png')
        self.parent_screen = parent_screen

    def spawn(self):
        self.parent_screen.blit(self.image, (self.x, self.y))


class Snake:
    def __init__(self, parent_screen, lenght):
        self.parent_screen = parent_screen
        self.square = pygame.image.load("Images/square.png")
        self.head = pygame.image.load("Images/snake_head.png")
        self.x = [size]*lenght
        self.y = [size]*lenght
        self.direction = 'down'
        self.lenght = lenght
        self.fruit = Fruit(self.parent_screen)

    def show_score(self):
        font = pygame.font.Font('Images/pixel-font7.regular.ttf', 60)
        score = font.render(f"Score: {self.lenght-3}", True, (255,255,255))
        self.parent_screen.blit(score, (750, 5))
        pygame.display.flip()

    def draw(self):
        self.parent_screen.fill((82,135,55))
        self.parent_screen.blit(self.head, (self.x[0], self.y[0]))
        self.fruit.spawn()
        for i in range(1,self.lenght):
            self.parent_screen.blit(self.square, (self.x[i], self.y[i]))
        pygame.draw.rect(self.parent_screen, (60,99,40), (0,0,1024,64))
        pygame.draw.rect(self.parent_screen, (60,99,40), (0, 0, 64, 768))
        pygame.draw.rect(self.parent_screen, (60,99,40), (960, 0, 64, 768))
        pygame.draw.rect(self.parent_screen, (60,99,40), (0, 704, 1024, 64))
        self.show_score()
        pygame.display.flip()

    def move_up(self):
        if self.direction == "down":
            return
        self.direction = 'up'

    def move_down(self):
        if self.direction == "up":
            return
        self.direction = "down"

    def move_left(self):
        if self.direction == "right":
            return
        self.direction = "left"

    def move_right(self):
        if self.direction == "left":
            return
        self.direction = "right"

    def walk(self):
        if self.direction == "up":
            self.y[0] -= 64
            self.draw()
        if self.direction == "down":
            self.y[0] += 64
            self.draw()
        if self.direction == "left":
            self.x[0] -= 64
            self.draw()
        if self. direction == "right":
            self.x[0] += 64
            self.draw()

        for i in range(self.lenght-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


    def wall_collision(self):
        if self.x[0] == 960:
            return True
        if self.x[0] == 0:
            return True
        if self.y[0] == 704:
            return True
        if self.y[0] == 0:
            return True
        return False


    def collision(self, x1, x2, y1, y2):
        if x1 >= x2 and x1 < x2+size:
            if y1 >= y2 and y1 < y2+size:
                return True
        return False

    def increase_size(self):
        self.lenght += 1
        self.x.append(self.x[self.lenght-2])
        self.y.append(self.y[self.lenght-2])


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.lungime = 1024
        self.inaltime = 768
        self.screen = pygame.display.set_mode((self.lungime, self.inaltime))
        self.icon = pygame.image.load("Images/snake.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Snake")
        self.lenght = 3
        self.snake = Snake(self.screen,self.lenght)

    def start(self):
        ok = True
        self.screen.fill((82, 135, 55))
        font = pygame.font.Font("Images/pixel-font7.regular.ttf", 55)
        font2 = pygame.font.Font("Images/pixel-font7.regular.ttf", 200)
        font3 = pygame.font.Font("Images/pixel-font7.regular.ttf", 70)
        snake = font2.render("Snake", True, (60, 99, 40))
        difficulty = font.render("Choose difficulty:", True, (60, 99, 40))
        easy = font3.render("Easy", True, (60, 99, 40))
        medium = font3.render("Medium", True, (60, 99, 40))
        hard = font3.render("Hard", True, (60, 99, 40))
        start = font.render('Start', True, (255, 255, 255))
        exit = font.render('Exit', True, (255, 255, 255))
        self.screen.blit(snake, (250, 150))
        self.screen.blit(difficulty, (300, 350))
        self.screen.blit(easy, (150, 525))
        self.screen.blit(medium, (415, 525))
        self.screen.blit(hard, (730, 525))
        pygame.display.flip()
        while ok:
            for event in pygame.event.get():
                maus = pygame.mouse.get_pos()
                if maus[1] >= 500 and maus[0] >= 100:
                    if maus[1] <= 625 and maus[0] <= 341:
                        easy_button = pygame.draw.rect(self.screen, (60,99,40), (100, 500, 241,125))
                        easy = font3.render("Easy", True, (82,135,55))
                        self.screen.blit(easy, (150, 525))
                        pygame.display.flip()
                    else:
                        easy_button = pygame.draw.rect(self.screen, (82,135,55), (100, 500, 241, 125))
                        easy = font3.render("Easy", True, (60,99,40))
                        self.screen.blit(easy, (150, 525))
                        pygame.display.flip()
                else:
                    easy_button = pygame.draw.rect(self.screen, (82, 135, 55), (100, 500, 241, 125))
                    easy = font3.render("Easy", True, (60, 99, 40))
                    self.screen.blit(easy, (150, 525))
                    pygame.display.flip()
                if maus[1] >= 500 and maus[0] >= 391:
                    if maus[1] <= 625 and maus[0] <= 632:
                        medium_button = pygame.draw.rect(self.screen, (60,99,40), (391, 500, 241,125))
                        medium = font3.render("Medium", True, (82,135,55))
                        self.screen.blit(medium, (415, 525))
                        pygame.display.flip()
                    else:
                        medium_button = pygame.draw.rect(self.screen, (82,135,55), (391, 500, 241, 125))
                        medium = font3.render("Medium", True, (60,99,40))
                        self.screen.blit(medium, (415, 525))
                        pygame.display.flip()
                else:
                    medium_button = pygame.draw.rect(self.screen, (82, 135, 55), (391, 500, 241, 125))
                    medium = font3.render("Medium", True, (60, 99, 40))
                    self.screen.blit(medium, (415, 525))
                    pygame.display.flip()
                if maus[1] >= 500 and maus[0] >= 682:
                    if maus[1] <= 625 and maus[0] <= 923:
                        hard_button = pygame.draw.rect(self.screen, (60,99,40), (682, 500, 241,125))
                        hard = font3.render("Hard", True, (82,135,55))
                        self.screen.blit(hard, (730, 525))
                        pygame.display.flip()
                    else:
                        hard_button = pygame.draw.rect(self.screen, (82,135,55), (682, 500, 241, 125))
                        hard = font3.render("Hard", True, (60,99,40))
                        self.screen.blit(hard, (730, 525))
                        pygame.display.flip()
                else:
                    hard_button = pygame.draw.rect(self.screen, (82, 135, 55), (682, 500, 241, 125))
                    hard = font3.render("Hard", True, (60, 99, 40))
                    self.screen.blit(hard, (730, 525))
                    pygame.display.flip()
                if event.type == pygame.QUIT:
                    ok = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ok = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus = pygame.mouse.get_pos()
                    if maus[1] >= 500 and maus[0] >= 100:
                        if maus[1] <= 625 and maus[0] <= 341:
                            self.reset()
                            pygame.mouse.set_pos((1025,0))
                            time.sleep(0.7)
                            if self.run(0.2) == False:
                                ok = False
                    if maus[1] >= 500 and maus[0] >= 391:
                        if maus[1] <= 625 and maus[0] <= 632:
                            self.reset()
                            pygame.mouse.set_pos((1025, 0))
                            time.sleep(0.7)
                            if self.run(0.15) == False:
                                ok = False
                    if maus[1] >= 500 and maus[0] >= 682:
                        if maus[1] <= 625 and maus[0] <= 923:
                            self.reset()
                            pygame.mouse.set_pos((1025, 0))
                            time.sleep(0.7)
                            if self.run(0.1) == False:
                                ok = False



    def show_gmover(self):
        self.screen.fill((82,135,55))
        pygame.draw.rect(self.screen, (60, 99, 40), (0, 0, 1024, 64))
        self.snake.show_score()
        font = pygame.font.Font('Images/pixel-font7.regular.ttf', 150)
        show1 = font.render(f"Game over!", True, (60,99,40))
        self.screen.blit(show1, (150, 200))
        main_menu = pygame.draw.rect(self.screen, (82, 135, 55), (180,500,241,125))
        restart = pygame.draw.rect(self.screen, (82, 135, 55), (601, 500, 241, 125))
        font = pygame.font.Font("Images/pixel-font7.regular.ttf", 65)
        main = font.render("Main", True, (60,99,40))
        menu = font.render("Menu", True, (60,99,40))
        restart = font.render("Restart", True, (60,99,40))
        self.screen.blit(main, (240, 507))
        self.screen.blit(menu, (230, 560))
        self.screen.blit(restart, (611, 530))
        pygame.display.flip()
        ok = True
        while ok:
            mouse = pygame.mouse.get_pos()
            if mouse[1] >= 500 and mouse[0] >= 180:
                if mouse[1] <= 625 and mouse[0] <= 420:
                    main_menu = pygame.draw.rect(self.screen, (60,99,40), (180, 500, 241, 125))
                    main = font.render("Main", True, (82, 135, 55))
                    menu = font.render("Menu", True, (82, 135, 55))
                    self.screen.blit(main, (240, 507))
                    self.screen.blit(menu, (230, 560))
                    pygame.display.flip()
                else:
                    main_menu = pygame.draw.rect(self.screen, (82, 135, 55), (180, 500, 241, 125))
                    main = font.render("Main", True, (60, 99, 40))
                    menu = font.render("Menu", True, (60, 99, 40))
                    self.screen.blit(main, (240, 507))
                    self.screen.blit(menu, (230, 560))
                    pygame.display.flip()
            else:
                main_menu = pygame.draw.rect(self.screen, (82, 135, 55), (180, 500, 241, 125))
                main = font.render("Main", True, (60, 99, 40))
                menu = font.render("Menu", True, (60, 99, 40))
                self.screen.blit(main, (240, 507))
                self.screen.blit(menu, (230, 560))
                pygame.display.flip()
            if mouse[1] >= 500 and mouse[0] >= 601:
                if mouse[1] <= 625 and mouse[0] <= 842:
                    restart = pygame.draw.rect(self.screen, (60, 99, 40), (601, 500, 241, 125))
                    restart = font.render("Restart", True, (82, 135, 55))
                    self.screen.blit(restart, (611, 530))
                    pygame.display.flip()
                else:
                    restart = pygame.draw.rect(self.screen, (82, 135, 55), (601, 500, 241, 125))
                    restart = font.render("Restart", True, (60, 99, 40))
                    self.screen.blit(restart, (611, 530))
                    pygame.display.flip()
            else:
                restart = pygame.draw.rect(self.screen, (82, 135, 55), (601, 500, 241, 125))
                restart = font.render("Restart", True, (60, 99, 40))
                self.screen.blit(restart, (611, 530))
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[1] >= 500 and mouse[0] >= 180:
                        if mouse[1] <= 625 and mouse[0] <= 420:
                            return 1
                    if mouse[1] >= 500 and mouse[0] >= 601:
                        if mouse[1] <= 625 and mouse[0] <= 842:
                            return 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 0
                    if event.key == pygame.K_RETURN:
                        return 2


    def play(self, seconds):
        self.snake.walk()
        time.sleep(seconds)
        for i in range(3, self.snake.lenght):
            if self.snake.collision(self.snake.x[0], self.snake.x[i], self.snake.y[0], self.snake.y[i]):
                sound = pygame.mixer.Sound("Images/tail_bite.wav")
                pygame.mixer.Sound.play(sound)
                raise Exception
        if self.snake.collision(self.snake.x[0],self.snake.fruit.x, self.snake.y[0], self.snake.fruit.y):
            sound = pygame.mixer.Sound("Images/eating_sound.wav")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_size()
            self.snake.fruit.x = random.randint(64, 896) // 64 * 64
            self.snake.fruit.y = random.randint(64, 704) // 64 * 64
            ct = 0
            while ct <= 5 and  self.snake.fruit.x in self.snake.x and self.snake.fruit.y in self.snake.y:
                self.snake.fruit.x = random.randint(64, 896) // 64 * 64
                self.snake.fruit.y = random.randint(64, 640) // 64 * 64
                ct += 1
                self.snake.fruit.spawn()
                #ct <= 30 and


    def reset(self):
        self.lenght = 3
        self.snake = Snake(self.screen, self.lenght)
        self.snake.draw()

    def run(self, seconds):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset()
                        pause = False
                    if event.key == pygame.K_ESCAPE:
                        self.screen.fill((82, 135, 55))
                        font = pygame.font.Font("Images/pixel-font7.regular.ttf", 55)
                        font2 = pygame.font.Font("Images/pixel-font7.regular.ttf", 200)
                        font3 = pygame.font.Font("Images/pixel-font7.regular.ttf", 70)
                        snake = font2.render("Snake", True, (60, 99, 40))
                        difficulty = font.render("Choose difficulty:", True, (60, 99, 40))
                        easy = font3.render("Easy", True, (60, 99, 40))
                        medium = font3.render("Medium", True, (60, 99, 40))
                        hard = font3.render("Hard", True, (60, 99, 40))
                        start = font.render('Start', True, (255, 255, 255))
                        exit = font.render('Exit', True, (255, 255, 255))
                        self.screen.blit(snake, (250, 150))
                        self.screen.blit(difficulty, (300, 350))
                        self.screen.blit(easy, (150, 525))
                        self.screen.blit(medium, (415, 525))
                        self.screen.blit(hard, (730, 525))
                        pygame.display.flip()
                        running = False
                        pause = True
                    if not pause:
                        if event.key == pygame.K_UP:
                            self.snake.move_up()
                        if event.key == pygame.K_DOWN:
                            self.snake.move_down()
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()
            if not pause:
                if self.snake.wall_collision():
                    pause = True
                    sound = pygame.mixer.Sound("Images/crash.wav")
                    pygame.mixer.Sound.play(sound)
                    indice = self.show_gmover()
                    if indice == 0:
                        return False
                    elif indice == 1:
                        self.screen.fill((82, 135, 55))
                        font = pygame.font.Font("Images/pixel-font7.regular.ttf", 55)
                        font2 = pygame.font.Font("Images/pixel-font7.regular.ttf", 200)
                        font3 = pygame.font.Font("Images/pixel-font7.regular.ttf", 70)
                        snake = font2.render("Snake", True, (60, 99, 40))
                        difficulty = font.render("Choose difficulty:", True, (60, 99, 40))
                        easy = font3.render("Easy", True, (60, 99, 40))
                        medium = font3.render("Medium", True, (60, 99, 40))
                        hard = font3.render("Hard", True, (60, 99, 40))
                        start = font.render('Start', True, (255, 255, 255))
                        exit = font.render('Exit', True, (255, 255, 255))
                        self.screen.blit(snake, (250, 150))
                        self.screen.blit(difficulty, (300, 350))
                        self.screen.blit(easy, (150, 525))
                        self.screen.blit(medium, (415, 525))
                        self.screen.blit(hard, (730, 525))
                        pygame.display.flip()
                        running = False
                        pause = True
                    elif indice == 2:
                        self.reset()
                        pause = False
                        pygame.mouse.set_pos((1025, 0))
                        time.sleep(0.7)
            try:
                if not pause:
                    self.play(seconds)
            except Exception:
                pause = True
                indice = self.show_gmover()
                if indice == 0:
                    return False
                elif indice == 1:
                    self.screen.fill((82, 135, 55))
                    font = pygame.font.Font("Images/pixel-font7.regular.ttf", 55)
                    font2 = pygame.font.Font("Images/pixel-font7.regular.ttf", 200)
                    font3 = pygame.font.Font("Images/pixel-font7.regular.ttf", 70)
                    snake = font2.render("Snake", True, (60, 99, 40))
                    difficulty = font.render("Choose difficulty:", True, (60, 99, 40))
                    easy = font3.render("Easy", True, (60, 99, 40))
                    medium = font3.render("Medium", True, (60, 99, 40))
                    hard = font3.render("Hard", True, (60, 99, 40))
                    start = font.render('Start', True, (255, 255, 255))
                    exit = font.render('Exit', True, (255, 255, 255))
                    self.screen.blit(snake, (250, 150))
                    self.screen.blit(difficulty, (300, 350))
                    self.screen.blit(easy, (150, 525))
                    self.screen.blit(medium, (415, 525))
                    self.screen.blit(hard, (730, 525))
                    pygame.display.flip()
                    running = False
                    pause = True
                elif indice == 2:
                    self.reset()
                    pause = False
                    pygame.mouse.set_pos((1025, 0))
                    time.sleep(0.7)


if __name__ == '__main__':
    game = Game()
    game.start()
