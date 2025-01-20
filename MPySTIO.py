from st7735 import TFT
from sysfont import sysfont
from time import sleep

class Rules(object):
    def __init__(self, surface):
        # create a surface object
        self.surface = surface
        self.width   = self.surface.size()[0]
        self.height  = self.surface.size()[1]
        self.x       = 0
        self.y       = 0
        
    def out(self, text):
        self.surface.text((self.x, self.y), text, TFT.WHITE, sysfont, 1)
        
        # detect the length of the string
        self.long    = len(text)
        self.char    = int(self.width / 6)
        self.storage = []
        
        if self.long > self.char:
            for i in range(int(self.long / self.char) + 1):
                self.storage.append(text[i * self.char:(i + 1) * self.char])
            
            self.y += len(self.storage) * 9 - 9
            
        self.y += 9
        
        # detect clean the surface
        self.lines =  ''.join(self.storage[int(self.height / 9):])
        
        if self.y > self.height:
            self.surface.fill(TFT.BLACK)
            self.y = 0
            
            self.out(self.lines)
            
    def get(self, text, keyboard, end):
        self.surface.text((self.x, self.y), text, TFT.WHITE, sysfont, 1)
        
        # buffer variable storage
        self.buffer = ''
        
        self.x += len(text) * 6
        
        # listen to the keyboard
        while True:
            self.keyboard = keyboard()
            sleep(0.12)
            
            if self.keyboard == end:
                self.y += 9
                if int(self.y / 9) >= int(self.height / 9):
                    self.surface.fill(TFT.BLACK)
                    self.x = 0
                    self.y = 0
                    
                    return self.buffer
                    
                self.x  = 0
                
                return self.buffer
            
            if self.keyboard is not None:
                if int(self.y / 9) >= int(self.height / 9):
                    self.surface.fill(TFT.BLACK)
                    self.y = 0
                
                self.surface.text((self.x, self.y), self.keyboard, TFT.WHITE, sysfont, 1)
                
                self.x += 6
                if int(self.x / 6) >= int(self.width / 6):
                    self.y += 9
                    self.x = 0
                    
                self.buffer += self.keyboard
