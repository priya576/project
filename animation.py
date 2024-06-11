import time
import adafruit_imageload
import adafruit_displayio_ssd1306
import board
import busio
import displayio
import i2cdisplaybus

IMAGE_FILE = "../icon_48_frames.bmp"
SPRITE_SIZE = (64,64)
FRAMES = 28

def invert_colors():
    temp = icon_pal[0]
    icon_pal[0] = icon_pal[1]
    icon_pal[1] = temp

displayio.release_displays()

sda, scl = board.SDA, board.SCL
i2c = busio.I2C(scl, sda)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address = 0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width = 128, height = 64)

group = displayio.Group()

icon_bit, icon_pal = adafruit_imageload.load(IMAGE_FILE, bitmap= displayio.Bitmap, palette = displayio.Palette)

invert_colors()

icon_grid = displayio.TileGrid(icon_bit, pixel_shader = icon_pal, width=1, height=1, tile_height = SPRITE_SIZE[1], tile_width = SPRITE_SIZE[0], default_tile=0, x=32, y=0)

group.append(icon_grid)

display.root_group = group

timer = 0.0
pointer = 0

while True:
    if (timer +0.1) < time.monotonic():
        icon_grid[0] = pointer
        pointer+=1
        timer = time.monotonic()
        if pointer > FRAMES - 1:
            pointer = 0
