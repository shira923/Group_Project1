game_field = []
FIELD_ROWS = 25
FIELD_COLS = 50
EMPTY_SQUARE = "EMPTY"


def create_game_field():
    global game_field
    for row in range(FIELD_ROWS):
        row = []
        for col in range(FIELD_COLS):
            row.append(EMPTY_SQUARE)
        game_field.append(row)

