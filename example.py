from MPySTIO import Rules
from machine import SPI, Pin
from ST7735 import TFT

# follow the actual settings
spi = SPI(1, sck = Pin(22), mosi = Pin(21), baudrate = 4000000)  
tft = TFT(spi, 5, 19, 23)  

tft.initr()  
tft.rgb(True)
tft.fill(TFT.BLACK)

# a basic output
screen = Rules(tft)
screen.out("Hello World")

# a basic input
# 
# text (A prompt for input is displayed)
# keyboard (Keyboard handlers)
# end (Return the result when "keyboard = ..." returns the string you write)
def get_key():
    pass

text = screen.get(text = 'Input Here>', keyboard = get_key, end = 'enter')
screen.out(text)
