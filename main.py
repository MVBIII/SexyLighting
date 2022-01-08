import board
import neopixel


# LED strip configuration:
LED_COUNT   = 150      # Number of LED pixels.
LED_PIN     = board.D18      # GPIO pin
LED_BRIGHTNESS = 0.2  # LED brightness
LED_ORDER = neopixel.RGB # order of LED colours. May also be RGB, GRBW, or RGBW

# Create an led strip and fill it with white
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=False, pixel_order = LED_ORDER)
strip.fill((255,0,0))
strip.show()
red= 97
green=93
blue=182
redstep=1
greenstep=2
bluestep=3
# while True:
#     red+=redstep
#     green+=greenstep
#     blue+=bluestep
#     if red>250 or red<3:
#         redstep = -redstep
#     if green>250 or green<3:
#         greenstep = -greenstep
#     if blue>250 or blue<3:
#         bluestep = -bluestep
strip.fill((green, red , blue))
strip.show()
