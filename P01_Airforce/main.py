"""
飞机大战主程序
V1.0
"""
import pygame as pg
import sys
from pygame.locals import *
import hero


class Background():
    """
    背景类，背景可以根据游戏等级切换关卡背景
    背景可以移动首尾相接
    """

    def __init__(self, bg_size, level):
        self.bg_height = bg_size[1]
        # 根据关卡等级加载不同的背景图片
        if level == 1:
            self.image1 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_1.jpg").convert()
            self.image2 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_1.jpg").convert()
        elif level == 2:
            self.image1 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_2.jpg").convert()
            self.image2 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_2.jpg").convert()
        elif level == 3:
            self.image1 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_3.jpg").convert()
            self.image2 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_3.jpg").convert()
        elif level == 4:
            self.image1 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_4.jpg").convert()
            self.image2 = pg.image.load(
                r"P01_Airforce\images\img_bg_level_4.jpg").convert()
        # 获取背景矩形
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        # 两种背景图片首尾相接位置初始化
        self.rect1.left, self.rect1.top = (0, 0)
        self.rect2.left, self.rect2.top = (0, self.bg_height)

        self.rect1.top = 0  # 第一张图片从0 开始移动
        self.rect2.top = -self.bg_height  # 第二张图片从底部开始移动

    def move(self):
        self.rect1.top += 1
        self.rect2.top += 1
        if self.rect1.top >= self.bg_height:
            self.rect1.top = 0
        if self.rect2.top >= 0:
            self.rect2.top = -self.bg_height


def game_event_handel(player1, player2):
    # 偶尔触发事件用下面的方式判断
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    
    # 检测用户的键盘操作 经常触发的事件采用下面的方式效率更高
    key_pressed = pg.key.get_pressed()
    # player1 按键控制检测
    if key_pressed[K_a]:
        player1.move_left()
    if key_pressed[K_d]:
        player1.move_right()
    if key_pressed[K_w]:
        player1.move_up()
    if key_pressed[K_s]:
        player1.move_down()
    # player2 按键控制检测
    if key_pressed[K_LEFT]:
        player2.move_left()
    if key_pressed[K_RIGHT]:
        player2.move_right()
    if key_pressed[K_UP]:
        player2.move_up()
    if key_pressed[K_DOWN]:
        player2.move_down()


def game_bg(bg, screen):
    """背景处理"""
    bg.move()
    screen.blit(bg.image1, bg.rect1)
    screen.blit(bg.image2, bg.rect2)


def game_hero_plane(hero, screen):
    # 英雄飞机处理
    screen.blit(hero.player_image, hero.player_rect)


def main():
    
    # 初始化pygame
    pg.init()
    # 设置背景窗口
    bg_size = bg_width, bg_height = 512, 768
    screen = pg.display.set_mode(bg_size)
    # 游戏等级初始化
    level = 1
    # 创建背景
    bg = Background(bg_size, level)
    # 设置窗口名称
    pg.display.set_caption("飞机大战")
    # 设置帧率
    fps = 60
    clock = pg.time.Clock()

    # 创建英雄飞机
    player1 = hero.HeroPlane(bg_size, 1)
    player2 = hero.HeroPlane(bg_size, 2)
    # 游戏循环
    running = True
    while running:
        clock.tick(fps)  # 设置刷新频率
        # 事件检测
        game_event_handel(player1, player2)
        # 绘制背景
        game_bg(bg, screen)
        # 绘制玩家飞机
        game_hero_plane(player1, screen)
        game_hero_plane(player2, screen)
        # 绘制玩家子弹
        # 绘制敌人飞机
        # 绘制敌人子弹
        # 显示所有元素到屏幕
        pg.display.flip()


if __name__ == "__main__":
    main()
