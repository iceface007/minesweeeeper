import pygame

import game
import ui

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Minesweeper")


    first_click  = True
    cell_size = 40
    grid_width, grid_height = 10, 10
    mines = 99
    field = game.create_field(grid_width, grid_height, mines)
    game.count_mines_around(field, grid_width, grid_height)
    revealed = [[False for _ in range(grid_width)] for _ in range(grid_height)]
    flags = [[False for _ in range(grid_width)] for _ in range(grid_height)]

    font = pygame.font.Font(None, 36)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grid_x, grid_y = x // cell_size, y // cell_size

                if event.button == 1:  # Linke Maustaste
                    message, game_over = game.reveal_field(field, revealed, grid_x, grid_y, grid_width, grid_height, first_click)
                    first_click = False
                    print(message)
                    if game_over:
                        running = False
                elif event.button == 3:  # Rechte Maustaste
                    flags[grid_y][grid_x] = not flags[grid_y][grid_x]

        ui.update_display(screen, field, revealed, flags, cell_size, font)

        # Überprüfen, ob das Spiel gewonnen wurde
        game_status = game.check_game_over(revealed, field, grid_width, grid_height, mines)
        if game_status == "won":
            print("Glückwunsch! Du hast gewonnen!")
            running = False
        elif game_status == "lost":
            print("Leider verloren. Viel Erfolg beim nächsten Mal!")
            running = False

        # Pygame-Fenster aktualisieren
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
