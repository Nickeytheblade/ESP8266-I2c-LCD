from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

#i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

grin = bytearray([0x00,0x00,0x0A,0x00,0x1F,0x11,0x0E,0x00])
full = bytearray([0x0E,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F])  # 100% Full
duck = bytearray([0x00,0x0c,0x1d,0x0f,0x0f,0x06,0x00,0x00])
heart = bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00])
face = bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00])
lcd.custom_char(0, heart)
lcd.custom_char(1, face)
lcd.custom_char(2,duck)
lcd.custom_char(3,full)
lcd.custom_char(4,grin)
lcd.putstr(chr(2)+" Hacker House "+chr(2)+chr(1)+" "+chr(1)+" "+chr(1)+" "+chr(1)+" "+chr(1)+" "+chr(1)+" "+chr(1)+" "+chr(1))
