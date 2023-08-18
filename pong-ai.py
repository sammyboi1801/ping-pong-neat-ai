# from pong import Pong
import pygame
import neat
import os
import time
import pickle
import random





class PongAI:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ping Pong AI")
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


    def train_ai(self,genome1,genome2,config):
        self.game_status = 1
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False



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
                # self.initialize()
                # return self.player1_score,self.player2_score
                pass
                # text1 = self.font.render('Start Game', True, "white")
                # text2 = self.font.render('Press space to start',True,"white")
                # self.screen.blit(text1, (550, 300))
                # self.screen.blit(text2, (450, 400))
                # pygame.display.flip()
                # self.clock.tick(60)
                # continue

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
                return False

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            self.ball_animation()

            output1 = net1.activate((self.player1.x, self.ball.x, abs(self.player1.y - self.ball.y)))
            decision1 = output1.index(max(output1))

            if decision1 == 0:
                pass
            elif decision1 == 1:
                if self.player1.x+10>1280 - 150:
                    pass
                else:
                    self.player1.x += 10
            else:
                if self.player1.x-10<0:
                    pass
                else:
                    self.player1.x -= 10

            output2 = net2.activate((self.player2.x, self.ball.x, abs(self.player2.y - self.ball.y)))
            decision2 = output2.index(max(output2))

            if decision2 == 0:
                pass
            elif decision2 == 1:
                if self.player2.x + 10 > 1280 - 150:
                    pass
                else:
                    self.player2.x += 10
            else:
                if self.player2.x - 10 < 0:
                    pass
                else:
                    self.player2.x -= 10

            # print(output1, output2)

            if self.player1_score>=1 or self.player2_score>=1 or self.player1_score>50:
                self.calculate_fitness(genome1,genome2,[self.player1_score,self.player2_score])
                break

            pygame.draw.line(self.screen, "red", (self.ball.x + 10, self.ball.y + 10), (self.player1.x + 75,self.player1.y))
            pygame.draw.line(self.screen, "orange", (self.ball.x + 10, self.ball.y + 10),(self.player2.x + 75, self.player2.y+10))

            pygame.display.flip()
            # self.clock.tick(120)


    def calculate_fitness(self,genome1,genome2,game_info):
        genome1.fitness+=game_info[0]
        genome2.fitness+=game_info[1]

    def testAI(self, genome, config):

        net = neat.nn.FeedForwardNetwork.create(genome,config)


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.screen.fill("purple")
            pygame.draw.rect(self.screen, "white", (0,self.screen.get_height()//2, 1280, 1))
            pygame.draw.rect(self.screen,"orange",self.player1)
            pygame.draw.rect(self.screen,"red",self.player2)
            pygame.draw.ellipse(self.screen,"white",self.ball)


            score2 = self.score_font.render(f"AI Score: {self.player2_score}", True, "white")
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
                self.clock.tick(120)
                continue

            if self.game_status == 2:
                if self.player1_score>self.player2_score:
                    text1 = self.font.render('Orange won', True, "white")
                elif self.player1_score<self.player2_score:
                    text1 = self.font.render('Red won', True, "white")
                elif self.player1_score==self.player2_score:
                    if self.ball.y >= 685:
                        text1 = self.font.render('Red won', True, "white")
                    else:
                        text1 = self.font.render('Orange won', True, "white")


                text2 = self.font.render('Press space to start',True,"white")
                self.screen.blit(text1, (550, 300))
                self.screen.blit(text2, (450, 400))
                pygame.display.flip()
                self.clock.tick(120)
                continue

            # if self.keys[pygame.K_LEFT]:
            #     if self.player1.x-10<0:
            #         pass
            #     else:
            #         self.player1.x -= 10
            # if self.keys[pygame.K_RIGHT]:
            #     if self.player1.x+10>1280 - 150:
            #         pass
            #     else:
            #         self.player1.x += 10

            output = net.activate((self.player2.x, self.ball.x, abs(self.player2.y - self.ball.y)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                if self.player2.x + 10 > 1280 - 150:
                    pass
                else:
                    self.player2.x += 10
            else:
                if self.player2.x - 10 < 0:
                    pass
                else:
                    self.player2.x -= 10

            if self.keys[pygame.K_a]:
                if self.player1.x-10<0:
                    pass
                else:
                    self.player1.x -= 10

            if self.keys[pygame.K_d]:
                if self.player1.x+10>1280 - 150:
                    pass
                else:
                    self.player1.x += 10

            if self.ball.y>=685 or self.ball.y<=20:
                self.game_status=2

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            self.ball_animation()

            pygame.draw.line(self.screen, "orange", (self.ball.x + 10, self.ball.y + 10),
                             (self.player2.x + 75, self.player2.y + 10))

            pygame.display.flip()
            self.clock.tick(120)


def eval_genomes(genomes,config):
    width,height = 1280, 720
    window = pygame.display.set_mode((width,height))

    for i,(genome_id1,genome1) in enumerate(genomes):
        print(i)
        if i==len(genomes)-1:
            break
        genome1.fitness=0
        for genome_id2,genome2 in genomes[i+1:]:
            genome2.fitness=0 if genome2.fitness == None else genome2.fitness
            game = PongAI()
            force_quit = game.train_ai(genome1,genome2,config)
            if force_quit:
                quit()

def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-49')
    # p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes,1)
    with open("model.pickle","wb") as f:
        pickle.dump(winner,f)

def testing(config):
    with open("model.pickle","rb") as f:
        winner = pickle.load(f)

    PongAI().testAI(winner,config)


if __name__=="__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,"config.txt")

    config = neat.Config(neat.DefaultGenome,
                         neat.DefaultReproduction,
                         neat.DefaultSpeciesSet,
                         neat.DefaultStagnation,
                         config_path)
    # run_neat(config)
    # PongAI().testAI()
    testing(config)