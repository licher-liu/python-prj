import pygame as pg


class HeroPlane(pg.sprite.Sprite):  # 继承pygame精灵类
    """英雄飞机类"""
    def __init__(bg_size):
        # 初始化sprite
        pg.sprite.Sprite.__init__(self)

