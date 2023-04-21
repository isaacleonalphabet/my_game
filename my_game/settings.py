# File created by Isaac Leon 
WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False
# Starting platforms
# I amde a plat form and hcnaged their colors
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, RED, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
# The platform on the right states that there is an opneining on the left side of the game 
# Disappearing = when I touvh it, it will magicall disapear from existence. 
                 (350, 200, 100, 20, (200,200,200), "normal"), (100, HEIGHT - 100, WIDTH, 10, BLACK, "disappearing")]
                 
