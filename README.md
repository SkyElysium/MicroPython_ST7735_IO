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
The way to print:

```screen.out("Hello World")```

The way to input:

```screen.get(text = "input here", keyboard = ..., end = 'enter')```

> Notice: I won't keep updating this library. If you want to help, welcome you!
