import pygame
import random

class Pong:

    def __init__(self):
        pygame.init()


        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_status = 0
        self.font = pygame.font.Font('04B_19.TTF', 32)
        self.score_font = pygame.font.SysFont('artifaktelementregulartruetype',16)


        self.player_pos1 = pygame.Vector2(self.screen.get_width() // 2 - 75, 685)
        self.player_pos2 = pygame.Vector2(self.screen.get_width() // 2 - 75, 20)
        self.ball_pos = pygame.Vector2(self.screen.get_width() // 2, self.screen.get_height() // 2)

        self.ball = pygame.Rect(self.ball_pos.x - 10,self.ball_pos.y-10,20,20)
        self.player1 = pygame.Rect(self.player_pos1.x,self.player_pos1.y,150,15)
        self.player2 = pygame.Rect(self.player_pos2.x,self.player_pos2.y,150,15)
        self.player1_score = 0
        self.player2_score = 0

        # print(pygame.font.get_fonts())

        self.ball_speed_x = 5*random.choice([-1,1])
        self.ball_speed_y = 5*random.choice([-1,1])


    def initialize(self):
        self.player_pos1 = pygame.Vector2(self.screen.get_width() // 2 - 75, 685)
        self.player_pos2 = pygame.Vector2(self.screen.get_width() // 2 - 75, 20)
        self.ball_pos = pygame.Vector2(self.screen.get_width() // 2, self.screen.get_height() // 2)

        self.ball = pygame.Rect(self.ball_pos.x - 10, self.ball_pos.y - 10, 20, 20)
        self.player1 = pygame.Rect(self.player_pos1.x, self.player_pos1.y, 150, 15)
        self.player2 = pygame.Rect(self.player_pos2.x, self.player_pos2.y, 150, 15)
        self.player1_score = 0
        self.player2_score = 0

        # print(pygame.font.get_fonts())

        self.ball_speed_x = 5 * random.choice([-1, 1])
        self.ball_speed_y = 5 * random.choice([-1, 1])

    def ball_animation(self):
        if self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height():
            self.ball_speed_y *= -1
        if self.ball.left <= 0 or self.ball.right >= self.screen.get_width():
            self.ball_speed_x *= -1

        if self.ball.colliderect(self.player1):
            self.ball_speed_y *= -1
            self.player1_score+=1
        if self.ball.colliderect(self.player2):
            self.ball_speed_y *= -1
            self.player2_score += 1


    def play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.screen.fill("purple")
            pygame.draw.rect(self.screen, "white", (0,self.screen.get_height()//2, 1280, 1))
            pygame.draw.rect(self.screen,"orange",self.player1)
            pygame.draw.rect(self.screen,"red",self.player2)
            pygame.draw.ellipse(self.screen,"white",self.ball)


            score2 = self.score_font.render(f"Score: {self.player2_score}", True, "white")
            score1 = self.score_font.render(f"Score: {self.player1_score}", True, "white")
            self.screen.blit(score2, (1185, 50))
            self.screen.blit(score1, (1185, 650))



            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_SPACE]:
                if self.game_status == 2:
                    self.initialize()
                self.game_status = 1



            if self.game_status == 0:
                text1 = self.font.render('Start Game', True, "white")
                text2 = self.font.render('Press space to start',True,"white")
                self.screen.blit(text1, (550, 300))
                self.screen.blit(text2, (450, 400))
                pygame.display.flip()
                self.clock.tick(60)
                continue

            if self.game_status == 2:
                if self.player1_score>self.player2_score:
                    text1 = self.font.render('Red won', True, "white")
                elif self.player1_score>self.player2_score:
                    text1 = self.font.render('Orange won', True, "white")
                elif self.player1_score==self.player2_score:
                    if self.ball.y >= 685:
                        text1 = self.font.render('Red won', True, "white")
                    else:
                        text1 = self.font.render('Orange won', True, "white")
                text2 = self.font.render('Press space to start',True,"white")
                self.screen.blit(text1, (550, 300))
                self.screen.blit(text2, (450, 400))
                pygame.display.flip()
                self.clock.tick(60)
                continue

            if self.keys[pygame.K_LEFT]:
                if self.player1.x-10<0:
                    pass
                else:
                    self.player1.x -= 10
            if self.keys[pygame.K_RIGHT]:
                if self.player1.x+10>1280 - 150:
                    pass
                else:
                    self.player1.x += 10

            if self.keys[pygame.K_a]:
                if self.player2.x-10<0:
                    pass
                else:
                    self.player2.x -= 10

            if self.keys[pygame.K_d]:
                if self.player2.x+10>1280 - 150:
                    pass
                else:
                    self.player2.x += 10

            if self.ball.y>=685 or self.ball.y<=20:
                self.game_status=2

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            self.ball_animation()



            pygame.display.flip()
            self.clock.tick(60)

Pong().play()