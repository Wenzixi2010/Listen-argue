from moviepy.editor import *
import pygame, random, time
#
FPS = 60
#
class Main:
    def __init__(self, clip, screen, button, font, play, python_logo, gameover):
         self.clip = clip
         self.screen = screen
         self.but = button
         self.font = font
         self.over = gameover
        #  self.play = False
         self.wrong = 0
         self.wining = 0
         self.python_logo = python_logo
    def main(self):
        self.screen.blit(python_logo,(0, 0))
        app.text()
        app.button()
        pygame.display.update()
        time.sleep(1)
        app.random()
    def random(self):
        self.rd = (random.randint(1, 8))
        print('正确答案:',self.rd)
        if self.rd == 1:
            self.audio = r'.\Audio\东.mp3'
        if self.rd == 2:
            self.audio = r'.\Audio\东北.mp3'
        if self.rd == 3:
            self.audio = r'.\Audio\东南.mp3'
        if self.rd == 4:
            self.audio = r'.\Audio\北.mp3'
        if self.rd == 5:
            self.audio = r'.\Audio\南.mp3'
        if self.rd == 6:
            self.audio = r'.\Audio\西.mp3'
        if self.rd == 7:
            self.audio = r'.\Audio\西北.mp3'
        if self.rd == 8:
            self.audio = r'.\Audio\西南.mp3'
        time.sleep(0.5)
        app.play_music()
    def button(self):
        self.screen.blit(self.but, (0, 50))
        self.screen.blit(self.but, (250, 50))
        self.screen.blit(self.but, (500, 50))
        self.screen.blit(self.but, (0, 300))
        self.screen.blit(self.but, (250, 300))
        self.screen.blit(self.but, (500, 300))
        self.screen.blit(self.but, (0, 550))
        self.screen.blit(self.but, (250, 550))
    def text(self):
        rgb = (255, 250, 250)
        text = self.font.render('东', True, rgb)
        text1 = self.font.render('东北', True, rgb)
        text2 = self.font.render('东南', True, rgb)
        text3 = self.font.render('北', True, rgb)
        text4 = self.font.render('南', True, rgb)
        text5 = self.font.render('西', True, rgb)
        text6 = self.font.render('西北', True, rgb)
        text7 = self.font.render('西南', True, rgb)
        screen.blit(text, (70, 100))
        screen.blit(text1, (290, 100))
        screen.blit(text2, (540, 100))
        screen.blit(text3, (70, 350))
        screen.blit(text4, (320, 350))
        screen.blit(text5, (570, 350))
        screen.blit(text6, (40, 600))
        screen.blit(text7, (290, 600))
    def screen_in(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 10<=x<=200 and 55<=y<=240:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 1:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                   
            elif 255<=x<=440 and 55<=y<=240:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 2:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
            elif 510<=x<=680 and 55<=y<=240:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 3:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
            elif 10<=x<=200 and 300<=y<=500:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 4:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
            elif 255<=x<=440 and 300<=y<=500:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 5:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
            elif 510<=x<=680 and 300<=y<=500:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 6:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
            elif 10<=x<=200 and 560<=y<=740:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 7:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
            elif 255<=x<=440 and 560<=y<=740:
                print('你的答案:',self.rd)
                if self.wining == 3:
                    app.win()
                elif self.rd == 8:
                    self.wining += 1
                    app.random()
                else:
                    for i in range(1):
                        if self.wrong == 0:
                            wrong = VideoFileClip(r'.\Video\2.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 1:
                            wrong = VideoFileClip(r'.\Video\3.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.main()
                            break
                        elif self.wrong == 2:
                            wrong = VideoFileClip(r'.\Video\4.mp4')
                            wrong.preview()
                            self.wrong += 1
                            app.gameover()
                            break                  
    def play_music(self):
        self.play = True
        print(self.audio)
        pygame.mixer.music.load(self.audio)
        pygame.mixer.music.play(1)
        self.play = False
    def gameover(self):
        self.screen.blit(self.over, (0, 0))
    def win(self):
        win = VideoFileClip(r'.\Video\5.mp4')
        win.preview()
        win.close()
#
pygame.init()
pygame.mixer.init()
#
pygame.display.set_caption("听声辩位 -By Wenzixi")
screen = pygame.display.set_mode([1920, 1080])
clock = pygame.time.Clock()
#
font = pygame.font.Font(r'.\font\msyh.ttc', 60)
clip = VideoFileClip(r'.\Video\1.mp4')
python_logo = pygame.image.load(r'.\Image\python-logo.jpg').convert()
gameover = pygame.image.load(r'.\Image\gameover.jpg').convert()
button = pygame.image.load(r'.\Image\button.png').convert_alpha()
#
screen.blit(python_logo,(0, 0))
pygame.display.update()
time.sleep(1.5)
clip.preview()
#
play = None
app = Main(clip, screen, button, font, play, python_logo, gameover)
screen.blit(python_logo,(0, 0))
app.button()
app.text()
pygame.display.update()
time.sleep(1)
app.random()

exitFlag = False
step = 10
#

while not exitFlag:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitFlag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exitFlag = True
        #Test↓
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x,y)
    # 更新绘制到屏幕上
    # if play == True:
    #     print("don't touch")       
    # elif play == False:
    #     app.screen_in()
        app.screen_in(event)
    pygame.display.update()