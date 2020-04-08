import pygame as pg


class HeroPlane(pg.sprite.Sprite):  # 继承pygame精灵类
    """英雄飞机类"""

    def __init__(self, bg_size, player):
        # 初始化sprite
        pg.sprite.Sprite.__init__(self)
        # 获取背景大小
        self.bg_width, self.bg_height = bg_size
        self.player = player
        # 加载英雄飞机图片
        # 判断player
        # player1 初始化：
        if self.player == 1:  # =1 player 1 ；=2 player2
            self.player_image = pg.image.load(
                ".//P01_Airforce//images//hero.png").convert_alpha()
            self.player_rect = self.player_image.get_rect()
            # 初始化 player 1 位置
            self.player_rect.left = int(self.bg_width/4)
            self.player_rect.top = self.bg_height - self.player_rect.height
        # player2 初始化
        if self.player == 2:  # =1 player 1 ；=2 player2
            self.player_image = pg.image.load(
                ".//P01_Airforce//images//hero2.png").convert_alpha()
            self.player_rect = self.player_image.get_rect()
            self.player_rect.left = int(self.bg_width/4*3)
            self.player_rect.top = self.bg_height - self.player_rect.height

        # 飞机速度
        self.speed = 10
        # 初始化飞机位置 飞机1 在屏幕下方1/4处 ，飞机2 在3/4处

    """先做player1 的移动，后面再考虑player2的移动，测试效果"""

    def move_up(self):
        self.player_rect.top -= self.speed
        if self.player_rect.top <= 0:
            self.player_rect.top = 0

    def move_down(self):
        self.player_rect.bottom += self.speed
        if self.player_rect.bottom >= self.bg_height:
            self.player_rect.bottom = self.bg_height

    def move_left(self):
        self.player_rect.left -= self.speed
        if self.player_rect.left <= 0:
            self.player_rect.left = 0

    def move_right(self):
        # player1 移动
        self.player_rect.left += self.speed
        if self.player_rect.right >= self.bg_width:
            self.player_rect.right = self.bg_width
