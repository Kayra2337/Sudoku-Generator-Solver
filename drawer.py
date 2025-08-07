# sudoku_drawer.py
import matplotlib.pyplot as plt
import numpy as np

def draw_sudoku(board, filename="sudoku.png"):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xticks(np.arange(0.5, 9.5, 1))
    ax.set_yticks(np.arange(0.5, 9.5, 1))
    ax.grid(which='major', color='black', linewidth=2)

    # Beyaz arka plan
    ax.imshow(np.zeros((9,9)), cmap='Blues', vmin=0, vmax=1)

    # Hücrelere siyah renkte rakamları yaz
    for i in range(9):
        for j in range(9):
            val = board[i, j]
            if val != 0:
                ax.text(j, i, str(val), va='center', ha='center', fontsize=20, color='black')

    # Eksenleri gizle
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(8.5, -0.5)  # Y eksenini ters çevir ki üstten başlasın

    plt.savefig(filename)
    plt.close()