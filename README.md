# MicroPython_ST7735_IO

How to import this library:

```from MPySTIO import Rules```

Then, try creating a **screen object**

```screen = Rules(Your_TFT_Class)```

The way to print:

```screen.out("Hello World")```

The way to input:

```screen.get(text = "input here", keyboard = ..., end = 'enter')```
