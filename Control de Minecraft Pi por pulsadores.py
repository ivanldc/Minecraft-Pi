import RPi.GPIO as GPIO
import time
import pygame, sys
from pygame.locals import*
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pygame.init()
FPS = 30
FPSCLOCK = pygame.time.Clock()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(33, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(35, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while True:
    est = [GPIO.input(11),GPIO.input(13),GPIO.input(29),GPIO.input(31),GPIO.input(33),GPIO.input(35)]
    x, y, z = mc.player.getTilePos()
    mc.player.setTilePos(x + est [2] - est [3], y - est [0] + est [1], z - est [4] + est [5])
    FPSCLOCK.tick(FPS)
