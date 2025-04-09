# --- main.py ---

from ttkbootstrap import Style
from src.theme import carregar_tema_salvo
from src.ui import criar_interface


if __name__ == "__main__":
    tema = carregar_tema_salvo()
    style = Style(theme=tema)
    root = style.master
    root.title("Gerador de QR Code")
    root.geometry("600x700")

    criar_interface(root, style)

    root.mainloop()
