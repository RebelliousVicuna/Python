import pygame,random,sys
from pygame.locals import *
# 玩家操控的类对象，继承了“ 精灵类 ：pygame.sprite.Sprite”
class Player(pygame.sprite.Sprite):
    def __init__(self,screen_temp):
        super(Player, self).__init__()
        self.surf = pygame.Surface((40, 40))    # 默认对象大小
        self.surf.fill((255, 255, 255))         # 填充颜色
        self.rect = self.surf.get_rect()        # 获取矩阵的位置
        self.image=pygame.image.load("player1.jpg")     # 对象大小取决于图片大小
        self.screen=screen_temp

    # def display(self):
    #     self.screen.blit(self.image, self.rect)
    def update(self, pressed_keys):
        self.screen.blit(self.image, self.rect)     # 被update调用
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >=600:
            self.rect.bottom = 600



class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen_temp):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((66, 50))        #对象的大小
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))    # 位置随机生成
        self.image=pygame.image.load("enemy.jpg")
        self.screen=screen_temp
        self.speed = random.randint(1,3)
        # self.speed = 1
    def display(self):
        self.screen.blit(enemy.surf,enemy.rect)
    def update(self):
        self.screen.blit(enemy.surf, enemy.rect)
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        # if pygame.Rect.colliderect(self.rect,bullet.rect):
        #     self.kill()

class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen_temp):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((20, 20))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.x = player.rect.x+2
        self.rect.y = player.rect.y
        self.image = pygame.image.load("bullet.jpg")
        self.screen = screen_temp
        self.speed = 7

    def update(self):
        self.screen.blit(bullet.surf, bullet.rect)
        self.rect.move_ip(self.speed, 0)
        if self.rect.left >= 800:
            self.kill()

class Button():
    pass

# 写失败的类

# class Bullet(pygame.sprite.Sprite):
#     def __int__(self,screen_temp):
#         super(Bullet, self).__init__()
#         self.surf = pygame.Surface((20, 20))
#         self.rect = self.surf.get_rect()
#         self.image=pygame.image.load("bullet.jpg")
#         self.screen = screen_temp
#         self.speed = 7
#
#     def fire(self):
#         self.rect.centerx = player.rect.centerx  # 设置中心点x轴坐标
#         self.rect.left = player.rect.x +2
#     def update(self):
#         super().update()
#         self.screen.blit(bullet.image,bullet.rect)
#         self.rect.move_ip(self.speed, 0)
#         if self.rect.left>=600:
#             self.kill()
pygame.init()
pygame.display.set_caption("练习 ")                      # 命名
CREATE_ENEMY_EVENT = pygame.USEREVENT                   # 创建一个监听事件
CREATE_BULLET_EVENT = pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)         # 创建一个定时器（事件，时间间隔（毫秒））
pygame.time.set_timer(CREATE_BULLET_EVENT, 100)         # 创建一个定时器（事件，时间间隔（毫秒））
screen = pygame.display.set_mode((800, 600),0,32)       # 建立一个窗口(大小，功能（全屏FULLSCREEN一类的），分辨率)
bg=pygame.image.load("4.jpg")
text=pygame.font.SysFont("宋体",50)
i=0
check_dict=dict()
# my_text=text.render(str(i),1,(255,255,255))      # 返回一个 image 对象

player = Player(screen)
# enemy = Enemy(screen)
group_e = pygame.sprite.Group()
group_b = pygame.sprite.Group()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    enemy_hit_group = pygame.sprite.Group()         # 记录碰撞精灵组，用于添加爆炸特效
    # 检测碰撞函数
    # pygame.sprite.groupcollide(精灵组1,精灵组2,是否销毁精灵组1,是否销毁精灵组2)
    # 该函数返回一个字典<键为精灵组1，值为精灵组2>
    check_dict = pygame.sprite.groupcollide(group_e, group_b, True, True)
    i+=len(check_dict)                              # 得分
    my_text = text.render('Score: %s'%str(i), 1, (255, 255, 255))
    enemy_hit_group.add(check_dict)
    # 事件队列
    for event in pygame.event.get():
        if event.type == pygame.QUIT:               # 关闭窗口
            sys.exit()
        elif event.type == KEYDOWN:                 # 键盘事件
            if event.key == K_ESCAPE:               # esc退出
                sys.exit()
        elif event.type == CREATE_ENEMY_EVENT:      # 监听事件，重复发生，即每隔1000ms发生一次事件
            enemy = Enemy(screen)
            group_e.add(enemy)
            # group_e.update()
            # group_e.draw(screen)
        elif event.type == CREATE_BULLET_EVENT:
            bullet = Bullet(screen)
            group_b.add(bullet)
            # group_b.update()
            # group_b.draw(screen)
    #
    pressed_keys = pygame.key.get_pressed()
    screen.blit(bg, (0, 0))
    screen.blit(my_text, (600, 10))         # 得分对象
    group_e.update()                        # group 调用通用update函数
    group_e.draw(screen)                    # 调用draw函数（将对象的image 绘制到 形参（surface对象）里面）
    group_b.update()
    group_b.draw(screen)
    player.update(pressed_keys)             # 调用按键事件
    # enemy.update()
    # screen.blit(player.image,player.rect) # 将image 画到 目标rect上
    # screen.blit(enemy.surf,enemy.rect)
    # enemy.display()
    player.update(pressed_keys)
    pygame.display.update()                 # 更新画面
    # pygame.display.flip()


