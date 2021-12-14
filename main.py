import board
import neopixel


# LED strip configuration:
LED_COUNT   = 30      # Number of LED pixels.
LED_PIN     = board.D18      # GPIO pin
LED_BRIGHTNESS = 0.2  # LED brightness
LED_ORDER = neopixel.GRB # order of LED colours. May also be RGB, GRBW, or RGBW

# Create an led strip and fill it with white
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=False, pixel_order = LED_ORDER)
strip.fill((255,255,255))
strip.show()
