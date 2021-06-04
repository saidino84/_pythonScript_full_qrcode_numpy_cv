import pygame
import sys

class Jogador(object):
    def __init__(self,x:int=100,y:int=30,width:int=50,height:int=50,color:list=(255,255,24)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect=(self.x,self.y,self.width,self.height)
        
    
    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)
    
    def update():
        ...
        
    def move(self):
        key = pygame.key.get_pressed()
        # print('Moviment detected')
        
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            print(f'to- Left x:{self.x} Rect:{self.rect}')
            self.x-=4
            
            print(f'x={self.x}')
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x+=4
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y-=5
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.y+=5
        self.rect=(self.x,self.y,self.width,self.height)
        
class Game(object):
    def __init__(self,g_width:int=500,g_height:int=400,g_title:str="Socket mutiple_player Game"):
        self._display=pygame.display.set_mode((g_width,g_height))
        self.title=pygame.display.set_caption(g_title)
        self.start(start_=True)
        # self.jogador=Jogador()
    def draw(self):
        self._display.fill((123,76,53))
        rect=pygame.draw.rect(self._display,(12,33,123),(20,50,40,40))
        # self.jogador.draw(self._display)
        
    
     
        
    def start(self,start_:bool=True):
        while start_:
            self.draw()
            jogador=Jogador()
            jogador.draw(self._display)
            jogador.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # pygame.display.update()
            pygame.display.flip()
# def main():
         
if __name__ == "__main__":
    pygame.init()
    g=Game()         