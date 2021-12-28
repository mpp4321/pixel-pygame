from main import SCREEN_SIZE, N_SIZE
import pygame
import random
# this file is for palette / sprite / graphical stuff

def mult_tuple(tuple1, tuple2):
    return tuple(map(lambda x: x[0] * x[1], zip(tuple1, tuple2)))

def add_tuple(tuple1, tuple2):
    return tuple( map(lambda x: x[0] + x[1], zip(tuple1, tuple2)) )

def mod_tuple(tuple1, mod):
    return tuple(map(lambda x: x % mod, tuple1))

def _default_palette_value(_unused):
    return [(0,0,0) for _ in range(8)]

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bit o' bug")
    return screen

def random_floats():
    return (random.random(), random.random(), random.random())

def random_rgb():
    rgb = random.randint(0, 0xFFFFFF)
    return (0xFF & (rgb >> 4), 0xFF & (rgb >> 2), 0xFF & rgb)

# generate a random func with delta
def random_rgb_roll_over(delta=64):
    def __inner(rgb):
        dx_r = random.randint(-delta, delta)
        return tuple(map(lambda x: (x + dx_r) % 256, rgb))
    return __inner 

# generate a random func w/ no rollover just pos increase and max
def random_rgb_pos_increase(max_pos=8):
    def __inner(rgb):
        dx_r = random.randint(0, max_pos)
        return tuple(map(lambda x: min((x + dx_r), 255), rgb))
    return __inner 

# increase random r, g, b by triple mins
def multiple_rgb_random_increase_mod(r, g, b):
    def __inner(rgb):
        vals = (random.randint(0, r), random.randint(0, g), random.randint(0, b))
        return mod_tuple(add_tuple(rgb, vals), 256)
    return __inner 

# increase random r, g, b by triple mins no mod
def multiple_rgb_random_increase(r, g, b):
    def __inner(rgb):
        vals = (random.randint(0, r), random.randint(0, g), random.randint(0, b))
        return tuple(map(lambda x: min(255, x[0] + x[1]), zip(vals, rgb)))
    return __inner 



# return random 8 bit palette
def random_palette():
    random_palette = []
    for _ in range(8):
        # Generate random RGB
        random_palette.append(random_rgb())
    return random_palette

def load_palette_smart(texture, series_funcs=[]):
    unique_colors = set()
    palette_items = []
    for y in range(texture.get_height()):
        for x in range(texture.get_width()):
            pixel = texture.get_at((x, y))
            pixel = (pixel.r, pixel.g, pixel.b)
            if pixel not in unique_colors:
                unique_colors.add(pixel)
                for func in series_funcs:
                    pixel = func(pixel)
                pixel = mod_tuple(pixel, 255)
                palette_items.append(pixel)
                if len(palette_items) > 8:
                    return palette_items
    return palette_items

def load_image(filename):
    surf = pygame.image.load(filename).convert(8)
    surf.set_colorkey((255, 255, 255))
    return surf

def load_texture_with_color(filename, palette=_default_palette_value, **kwargs):
    global N_SIZE
    texture = load_image(filename)
    texture.set_palette(palette(texture, **kwargs))
    new_size = get_xy_rect(0, 0, N_SIZE)[2:]
    texture = pygame.transform.scale(texture, new_size)
    return texture

def poll_events():
    evs_polled = pygame.event.get()
    return evs_polled

# Get rect with n x n size onto screen
def get_xy_rect(x, y, n):
    global SCREEN_SIZE
    w_x = SCREEN_SIZE[0] // n
    w_y = SCREEN_SIZE[1] // n
    return (w_x * x, w_y * y, w_x, w_y)
