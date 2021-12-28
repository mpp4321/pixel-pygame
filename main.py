import pygame
import random
import palette

SCREEN_SIZE = (800, 800)
N_SIZE = 4
N_SIZE_RECT = (SCREEN_SIZE[0] / N_SIZE, SCREEN_SIZE[1] / N_SIZE)

if __name__ == "__main__":
    screen = palette.initialize_game()

    def do_some_palette(rgb):
        # fill screen with background color
        screen.fill((0x3F, 0x31, 0x1D))

        # fill screen w/ random palettes
        def process_pix(pixel):
            #return pixel
            # calculate brightness floats
            t_1 = tuple(map(lambda x: x / 255, pixel))
            #t_1 = random_floats()
            # apply it to a RGB pallette
            return palette.mult_tuple(t_1, rgb)
        
        def apply_randomness(pixel):
            t_1 = palette.random_floats()
            return palette.mult_tuple(t_1, pixel)
        
        def max_out(pixel):
            return tuple(map(lambda x: min(x, 255), pixel))
        
        def do_yellows(pix):
            avg = (pix[0] + pix[1]) / 2 
            return (avg, avg, pix[2])
        
        def shift_colors(pix):
            return (random.choice(pix), random.choice(pix), random.choice(pix))

        for y in range(N_SIZE):
            for x in range(N_SIZE):
                yx_rect = palette.get_xy_rect(x, y, N_SIZE)
                #player_spr = load_texture_with_color("behold.png", random_similar_palette(init=(0x3F, 0x31, 0x1D), delta=64))
                player_spr = palette.load_texture_with_color("player.png", palette=palette.load_palette_smart, series_funcs=[
                    apply_randomness, max_out
                ])
                screen.blit(player_spr, yx_rect)
                #screen.blit(load_texture_with_color("helmet_of_zargog.png", random_similar_palette(delta=4)), yx_rect)

        #pygame.image.save(screen, "test.png")
        pygame.display.flip()

    while True:
        evs = palette.poll_events()
        for ev in evs:
            if ev.type == pygame.KEYDOWN:
                # do_some_palette(random_rgb())
                # do_some_palette((0xff, 0xff, 0xff))
                do_some_palette((0x3F, 0x31, 0x1D))
                pass
        if any(map(lambda x: x.type == pygame.QUIT, evs)):
            break
