# MicroPython_ST7735_IO

The library depends on some other libraries:
- ST7735
- sysfont

## *Some Prepartion Work*
How to import this library:

```from MPySTIO import Rules```

Then, try creating a **screen object**

```screen = Rules(Your_TFT_Class)```

## *Functions*
1. The way to print:

```screen.out("Hello World")```

*If words are full of the screen, it will clean the screen and display the rest of the words.*

2. The way to input:

```screen.get(text = "input here", keyboard = ..., end = 'enter')```

*You need to write a function or any. Then, filled with the name of the function to fill into 'keyboard'.*
*'end' means it need to get somthing you write to end this input.*

> Notice: I won't keep updating this library. If you want to help, welcome you!
