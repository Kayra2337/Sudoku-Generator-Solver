import matplotlib.pyplot as plt
import numpy as np


def draw_sudoku(board, filename="sudoku.png"):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Beyaz arka plan
    ax.set_facecolor('white')

    # İnce çizgiler - her hücre arasına
    for i in range(10):
        lw = 2 if i % 3 == 0 else 0.8  # 3x3 blok çizgisi kalın, diğerleri ince
        # Dikey çizgiler
        ax.plot([i - 0.5, i - 0.5], [-0.5, 8.5], color='black', linewidth=lw)
        # Yatay çizgiler
        ax.plot([-0.5, 8.5], [i - 0.5, i - 0.5], color='black', linewidth=lw)

    # Sayıları hücrelerin ortasına yaz
    for i in range(9):
        for j in range(9):
            val = board[i, j]
            if val != 0:
                ax.text(j, i, str(val), va='center', ha='center', fontsize=20, color='black')

    # Eksenleri gizle (etiketler, çerçeve vb.)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(8.5, -0.5)  # Y eksenini ters çevir

    plt.savefig(filename)
    plt.close()
