import pygame
import pygame.freetype  # Import the freetype module.
import time
import random
import sys
pygame.init()

class console():
    def __init__(self,name,size,bgcolor,letter_color):
        self.bgcolor = bgcolor
        self.letter_color = letter_color
        self.size = size
        self.dis = pygame.display.set_mode((size[0]*8,size[1]*15))
        pygame.display.set_caption(name)
        self.screen_text = ''
        self.font_style = pygame.font.SysFont('Consolas', 15)

    def put_data(self,data):
        #dis.fill((0,0,0))
        #self.dis.blit(self.bg, (0, 0))
        data = data.split('\n')
        plus = 0
        for msg in range(len(data)):
            #z = pygame.event.get()
            #time.sleep(0.01)
            try:
                mesg = self.font_style.render(data[msg], True,  self.letter_color)
                self.dis.blit(mesg, [0, msg*15])
            except Exception as e:
                print(e)
            #plus += 1
            #print(data[msg])

    def text_add(self,data):
        self.screen_text += data

    def update(self):
        events = ''
        dat = self.screen_text.split('\n')
        while len(dat) > self.size[1]:
            del dat[0]
        self.screen_text = '\n'.join(dat)
        self.put_data(self.screen_text)
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key != pygame.K_RETURN:
                    events += i.unicode
                else:
                    events += '\n'
            elif i.type == 32787:
                pygame.display.quit()
                sys.exit(0)
                    
            return events

    def clear(self):
        self.dis.fill(self.bgcolor)
        pygame.display.update()
        
    def show_scans(self):
        out = ''
        chr_ = ''
        while chr_ != '\n':
            chr_ = self.update()
            if chr_:
                if chr_ != '\n' and chr_ == '\b' and out: 
                    self.screen_text = self.screen_text[:-1]
                    out = out[:-1]
                else:
                    out += chr_
                    self.screen_text += chr_
                self.clear()
                self.update()
        return out[:-1]

    def hidden_scans(self):
        out = ''
        chr_ = ''
        while chr_ != '\n':
            chr_ = self.update()
            if chr_:
                if chr_ != '\n':
                    out += chr_
                    self.screen_text += '*'
            self.put_data(self.screen_text)
                    
        self.screen_text += '\n'
        return out
