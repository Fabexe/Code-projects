from machine import Pin, I2C
import ssd1306

# using default address 0x3c
i2c = I2C(id=1, scl=Pin(27), sda=Pin(26))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Afficheur OLED', 0, 0, 1)
display.show()

display.poweroff()
display.poweron()
display.contrast(0)
display.contrast(255)
display.invert(1)
display.invert(0)
display.rect(1, 1, 128, 60, 1)
display.show()
