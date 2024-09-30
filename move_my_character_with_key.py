from pico2d import *


open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('SNES - Dragon Quest 3 JPN - Character Classes.png')



def handle_events():
    global running, dirX, dirY, animate

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                animate += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
                animate += 1
            elif event.key == SDLK_UP:
                dirY += 1
                animate += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
                animate += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                animate -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
                animate -= 1
            if event.key == SDLK_UP:
                dirY -= 1
                animate -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1
                animate -= 1

running = True
x = 800 // 2
y = 600 // 2
frame = 0
frame_gap_X = 256 // 16
frame_gap_Y = 216 // 9
dirX = 0
dirY = 0
animate = 0

while running:
    clear_canvas()

    bg.draw(800 // 2, 600 // 2)
    character.clip_draw(frame * frame_gap_X, 0, frame_gap_X, frame_gap_Y, x, y)

    update_canvas()
    handle_events()

    if animate:
        frame = (frame + 1) % 2

    x += dirX * 5
    y += dirY * 5
    delay(0.05)

close_canvas()