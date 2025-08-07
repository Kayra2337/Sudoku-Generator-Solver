import streamlit as st
from generator import generate_sudoku
from solver import solve
from drawer import draw_sudoku
from PIL import Image

st.set_page_config(page_title="Sudoku Uygulaması", layout="centered")
st.title("🧩 Sudoku Üretici & Çözücü")

if "grid" not in st.session_state:
    st.session_state.grid = None
if "message" not in st.session_state:
    st.session_state.message = ""

if st.button("🎲 Yeni Sudoku Üret"):
    st.session_state.grid = generate_sudoku()
    st.session_state.message = ""  # mesajı sıfırla sudoku üretince

if st.button("🧠 Sudoku Çöz"):
    if st.session_state.grid is not None:
        solved = solve(st.session_state.grid)
        if not solved:
            st.session_state.message = "Çözüm bulunamadı!"
        else:
            st.session_state.message = ""
    else:
        st.session_state.message = "Önce bir sudoku üretmelisin."

# Sudoku gösterimi
if st.session_state.grid is not None:
    draw_sudoku(st.session_state.grid, "sudoku_output.png")
    image = Image.open("sudoku_output.png")
    st.image(image, caption="Sudoku Tahtası", use_container_width=True)

    with open("sudoku_output.png", "rb") as f:
        st.download_button("📥 PNG Olarak İndir", f, file_name="sudoku.png", mime="image/png")

# Mesaj gösterimi (eğer varsa)
if st.session_state.message:
    st.info(st.session_state.message)
