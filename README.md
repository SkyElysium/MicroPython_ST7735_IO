# MicroPython_ST7735_IO

How to import this library:

```from MPySTIO import Rules```

Then, try creating a **screen object**

(```)python screen = Rules(Your_TFT_Class) (```)

The way to print:

(```)python screen.out("Hello World") (```)

The way to input:

(```)python screen.get(text = "input here", keyboard = ..., end = 'enter') (```)
