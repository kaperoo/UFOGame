import pygame
import os
import random

pygame.init()
winx = 600
winy = 600
pygame.display.set_caption("UFO")
screen = pygame.display.set_mode((winx, winy))
powierzchnia = pygame.Surface((winx, winy))
powierzchnia.set_colorkey((0, 0, 0))
powierzchnia.set_alpha(128)

#Functions for displaying text and images

def writeOnScreen(txt, size):
    font = pygame.font.SysFont("Arial", size)
    txt = font.render(txt, 1, (255, 255, 255))
    x = (winx - txt.get_rect().width) / 2
    y = (winy - txt.get_rect().height) / 2
    screen.blit(txt, (int(x), (int(y) + 43)))

def score(x, y, txt, size):
    font = pygame.font.SysFont("Arial", size)
    txt = font.render(txt, 1, (255, 255, 255))
    screen.blit(txt, (int(x), int(y)))

def hscore(y, txt, size):
    font = pygame.font.SysFont("Arial", size)
    txt = font.render(txt, 1, (255, 255, 255))
    x = (winx - txt.get_rect().width) / 2
    screen.blit(txt, (int(x), int(y)))

def backgr():          
    bg = pygame.image.load(os.path.join('tlo.png'))
    screen.blit(bg, (0, 0))

def backGame():          
    bg = pygame.image.load(os.path.join('tlod.png'))
    screen.blit(bg, (0, 0))

def gameover():
    go = pygame.image.load(os.path.join('go.png'))
    x = (winx - go.get_rect().width) / 2
    y = (winy - go.get_rect().height) / 2
    screen.blit(go, (x, y))

def logo():
    logo = pygame.image.load(os.path.join('logo.png'))
    x = (winx - logo.get_rect().width) / 2
    y = (winy - logo.get_rect().height) / 2
    screen.blit(logo, (x, y))

#Classes for asteroids and ufo  

class Asteroidy():
    def __init__(self, x, y, radius, vx, vy, rot):
        self.x = x
        self.y = y
        self.center = [self.x, self.y]
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.rot = rot
        self.kolor = (255, 0, 0, 0)
        self.kometa = pygame.image.load(os.path.join('kometa.png'))
        self.kometa.convert()
        self.kom = self.kometa
        self.procent = self.radius / 30
        self.kom = pygame.transform.rotozoom(self.kometa, self.rot * 90, self.procent)
##   self.cir=pygame.draw.circle(screen,self.kolor,self.center,self.radius,0)
##    def rysuj(self):
##        screen.blit(self.kom,(self.x-self.radius,self.y-self.radius))
    def ruch(self, vx, vy):
        self.x = self.x - vx
        self.y = self.y - vy
        self.center = [self.x, self.y]
        self.cir = pygame.draw.circle(powierzchnia, self.kolor, self.center, self.radius, 0)
        screen.blit(self.kom, (self.x-self.radius, self.y - self.radius))
    def kolizja(self, player):
        if self.cir.colliderect(player):
            return True
        else:
            return False

class Ufo():
    def __init__(self, x, y, rozm):
        self.x = x
        self.y = y
        self.rozm = rozm
        self.kolor = (0, 0, 255)
        self.ufko = pygame.image.load(os.path.join('ufo.png'))
        self.sq = pygame.Rect(self.x, self.y, self.rozm, self.rozm)
    def rysuj(self):
        screen.blit(self.ufko, (self.x, self.y))
        #pygame.draw.rect(screen,self.kolor,self.sq,0)
    def ruch(self, dx, dy, dx2, dy2):
        self.x = self.x - dx
        self.x = self.x - dx2
        self.y = self.y - dy
        self.y = self.y - dy2
        self.sq = pygame.Rect(self.x, self.y, self.rozm, self.rozm)

##############################################################

def main():
    asteroidy=[]
    ilosc=12
    copokazuje="menu"
    ufo=Ufo(290,290,20)
    #read=open("highscore.txt")
    #write=open("highscore.txt","w")
    highscore=0

    clock = pygame.time.Clock()

    while True:
        
        clock.tick(100)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_SPACE and copokazuje!="gra":
                    kurwa=True
                    kx=0
                    ky=0
                    kx2=0
                    ky2=0
                    copokazuje="gra"
                    wynik=0
                    
                if event.key==pygame.K_UP:
                    ky=3
                if event.key==pygame.K_DOWN:
                    ky2=-3
                if event.key==pygame.K_RIGHT:
                    kx=-3
                if event.key==pygame.K_LEFT:
                    kx2=3

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    ky=0
                if event.key==pygame.K_DOWN:
                    ky2=0
                if event.key==pygame.K_RIGHT:
                    kx=0
                if event.key==pygame.K_LEFT:
                    kx2=0
                    
        if ufo.x<=0:
            kx2=0
        if ufo.x>=580:
            kx=0
        if ufo.y<=0:
            ky=0
        if ufo.y>=580:
            ky2=0
            
        screen.fill((0,0,0))

        if copokazuje=="menu":
            backgr()
            logo()
            writeOnScreen("press 'space' to begin",20)
        elif copokazuje=="over":
            backgr()
            gameover()
            hscore(370,"your score: "+str(wynik),20)
            read=open("highscore.txt")
            hscore(390,"highscore: "+read.read(),20)
            read.close()
            ufo=Ufo(290,290,20)
            writeOnScreen("press 'space' to try again",20)
        elif copokazuje=="gra":
            backGame()
            ufo.rysuj()
            ufo.ruch(kx,ky,kx2,ky2)

            if kurwa==True:
                kurwa=False
                for i in range(ilosc):
                    rvx=random.randint(1,3)
                    rvy=random.randint(1,3)
                    rpromien=random.randint(10,30)
                    rrot=random.randint(1,4)
                    if i<(ilosc/2):
                        ry=random.randint(1,2)
                        if ry==1:
                            ry=31
                        else:
                            ry=569
                        rx=random.randint(31,569)
                        asteroidy.append(Asteroidy(rx,ry,rpromien,rvx,rvy,rrot))
                    if i>=(ilosc/2):
                        rx=random.randint(1,2)
                        if rx==1:
                            rx=31
                        else:
                            rx=569
                        ry=random.randint(31,569)
                        asteroidy.append(Asteroidy(rx,ry,rpromien,rvx,rvy,rrot))

            for a in asteroidy:
                #a.rysuj()
                a.ruch(a.vx,a.vy)
                pygame.time.delay(0)                    #<==========================
                if a.kolizja(ufo.sq):
                    asteroidy.clear()
                    copokazuje="over"
            for a in asteroidy:
                if a.x<=a.radius or a.x>=(600-a.radius):
                    a.vx=-a.vx
                    if a.vy>0 and a.y>(4+a.radius) and a.y<(596-a.radius):
                        a.y=a.y-3
                    elif a.vy<0 and a.y>(4+a.radius) and a.y<(596-a.radius):
                        a.y=a.y+3
                    wynik=wynik+1
                if a.y<=a.radius or a.y>=(600-a.radius):
                    a.vy=-a.vy
                    if a.vx>0 and a.x>(4+a.radius) and a.x<(596-a.radius):
                        a.x=a.x-3
                    elif a.vx<0 and a.x>(4+a.radius) and a.x<(596-a.radius):
                        a.x=a.x+3       
                    wynik=wynik+1
            score(540,570,str(wynik),20)
            read=open("highscore.txt")
            highscore=read.read()
            read.close()

            if wynik==200 or wynik==500:
                for i in range(2):
                    rvx=random.randint(1,3)
                    rvy=random.randint(1,3)
                    rpromien=random.randint(10,30)
                    rrot=random.randint(1,4)
                    if i==0:
                        ry=random.randint(1,2)
                        if ry==1:
                            ry=31
                        else:
                            ry=569
                        rx=random.randint(31,569)
                        asteroidy.append(Asteroidy(rx,ry,rpromien,rvx,rvy,rrot))
                    elif i==1:
                        rx=random.randint(1,2)
                        if rx==1:
                            rx=31
                        else:
                            rx=569
                        ry=random.randint(31,569)
                        asteroidy.append(Asteroidy(rx,ry,rpromien,rvx,rvy,rrot))
            
            if wynik > int(highscore):
                write=open("highscore.txt","w")
                write.write(str(wynik))
                write.close()
                
        pygame.display.update()

main()