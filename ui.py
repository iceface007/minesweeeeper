import pygame

# Pygame initialisieren und Konfigurationen setzen
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper made by Ilja")

# Farben
WHITE = (255, 255, 255)
GRAY = (190, 190, 190)
LIGHTER_GRAY = (215, 215, 215)
DARKER_GRAY = (156, 141, 141)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_grid(screen, field, revealed, flags, cell_size, font):
    for y in range(len(field)):
        for x in range(len(field[0])):
            smaller_rect = pygame.Rect(x * cell_size, y * cell_size, cell_size - 5, cell_size - 5)
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect)  # Zellenhintergrund
            pygame.draw.rect(screen, LIGHTER_GRAY, smaller_rect)  #Highlight  im unaufgedeckten Zellenhintergrund
            pygame.draw.rect(screen, BLACK, rect, 1)  # Umrandung

            if revealed[y][x]:
                if field[y][x] == -1:
                    pygame.draw.rect(screen, RED, rect)  # Mine anzeigen
                else:
                    pygame.draw.rect(screen, DARKER_GRAY, rect) # Aufgedecktes Feld
                    pygame.draw.rect(screen, BLACK, rect, 1)  # Umrandung
                    number_text = font.render(str(field[y][x]), True, BLACK)
                    screen.blit(number_text, number_text.get_rect(center=rect.center))
            elif flags[y][x]:
                flag_text = font.render('F', True, RED)
                screen.blit(flag_text, flag_text.get_rect(center=rect.center))

def update_display(screen, field, revealed, flags, cell_size, font):
    screen.fill(BLACK)  # Hintergrund löschen
    draw_grid(screen, field, revealed, flags, cell_size, font)  # Spielfeld zeichnen
    pygame.display.flip()  # Änderungen anzeigen
