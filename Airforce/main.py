"""
打飞机主程序
V1.0
"""
import pygame as pg

# 初始化pygame
pg.init()
# 设置背景窗口大小
screen_size = width, height = 480, 700
screen = pg.display.set_mode(screen_size)
# 设置窗口名称
pg.display.set_caption("飞机大战")
background = pg.image.load("images/bg.png").convert()
