import js
from pyodide.ffi import create_proxy
import asyncio
from pyodide.http import pyfetch

board = [""] * 9
current_player = "X"
game_over = False

async def send_result(winner):
    await pyfetch(
        url="/save_result",
        method="POST",
        headers={"Content-Type": "application/json"},
        body=f'{{"winner": "{winner}"}}'
    )


def make_move(index):
    global current_player, game_over
    status = Element("status")

    if game_over or board[index] != "":
        return

    board[index] = current_player
    Element(f"cell{index}").write(current_player)

    if check_winner():
        status.write(f"🏆 Player {current_player} wins!")
        asyncio.ensure_future(send_result(current_player))
        game_over = True
    elif "" not in board:
        status.write("😐 It's a draw!")
        asyncio.ensure_future(send_result("Draw"))
        game_over = True
    else:
        current_player = "O" if current_player == "X" else "X"
        status.write(f"Player {current_player}'s turn")


def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_conditions:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            return True
    return False


def reset_game(event=None):
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    for i in range(9):
        Element(f"cell{i}").write("")
    Element("status").write("Player X's turn")


# Expose functions to JavaScript via proxies so onclick handlers can call them
try:
    from js import window
    window.make_move = create_proxy(make_move)
    window.reset_game = create_proxy(reset_game)
except Exception:
    # If JS/window isn't available yet, ignore — PyScript will set up later
    pass
