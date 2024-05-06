import random


def create_field(width, height, mines):
    field = [[0 for _ in range(width)] for _ in range(height)]
    placed_mines = 0
    while placed_mines < mines:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if field[y][x] == 0:
            field[y][x] = -1
            placed_mines += 1

    return field


def reveal_field(field, revealed, x, y, width, height, first_click):
    # Überprüfen, ob die Koordinaten innerhalb des Feldes liegen
    if 0 <= x < width and 0 <= y < height:
        if revealed[y][x]:
            # Feld wurde bereits aufgedeckt
            return "Field already revealed.", False
        revealed[y][x] = True  # Feld als aufgedeckt markieren

        if field[y][x] == -1:
            if first_click:
                field[y][y] = 0
                return "Lucky its your first click", False

            # Eine Mine wurde aufgedeckt
            return "Boom! You hit a mine.", True
        elif field[y][x] == 0:
            # Automatisches Aufdecken aller angrenzenden Felder, wenn keine Minen angrenzen
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx != 0 or dy != 0) and 0 <= x + dx < width and 0 <= y + dy < height:
                        reveal_field(field, revealed, x + dx, y + dy, width, height, first_click)
        return f"Safe, {field[y][x]} mine(s) around.", False
    else:
        return "Invalid coordinates.", False


def check_game_over(revealed, field, width, height, mines):
    # Verloren, wenn auf eine Mine geklickt wurde
    for y in range(height):
        for x in range(width):
            if revealed[y][x] and field[y][x] == -1:
                return "lost"

    # Gewonnen, wenn alle Nicht-Minen-Felder aufgedeckt wurden
    safe_fields = width * height - mines
    revealed_count = sum(row.count(True) for row in revealed)

    if revealed_count == safe_fields:
        return "won"

    # Spiel geht weiter
    return "continue"


def count_mines_around(field, width, height):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for y in range(height):
        for x in range(width):
            if field[y][x] == -1:
                continue
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if field[ny][nx] == -1:
                        count += 1
            field[y][x] = count



