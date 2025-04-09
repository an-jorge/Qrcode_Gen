import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import PRIMARY, SECONDARY
from ttkbootstrap.widgets import Entry, Label, Button
from PIL import Image, ImageTk
import qrcode
import json
import os

# Caminho do arquivo de config
CONFIG_PATH = "config.json"

# Carrega tema salvo ou define padrão
def carregar_tema_salvo():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as file:
            dados = json.load(file)
            return dados.get("tema", "flatly")  # flatly = claro
    return "flatly"

# Salva o tema atual no arquivo
def salvar_tema(tema):
    with open(CONFIG_PATH, "w") as file:
        json.dump({"tema": tema}, file)

# Tema inicial (flatly = claro / darkly = escuro)
tema_atual = carregar_tema_salvo()
style = Style(theme=tema_atual)

# Janela principal
root = style.master
root.title("Gerador de QR Code")
root.geometry("600x700")

# Variáveis globais
imagem_ref = None
label_img = None
entrada_texto = tk.StringVar()

# Função para gerar o QR Code
def qr_generator(event=None):
    texto = entrada_texto.get()

    if not texto:
        error_label.config(text="O texto não pode estar vazio!")
        esconder_imagem()
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save("qr_code.png")

    error_label.config(text="")
    exibir_imagem()

# Mostrar imagem
def exibir_imagem():
    global imagem_ref, label_img

    imagem = Image.open("qr_code.png").resize((200, 200))
    imagem_ref = ImageTk.PhotoImage(imagem)

    if label_img is None:
        label_img = Label(root, image=imagem_ref)
        label_img.place(relx=0.5, rely=0.75, anchor="center")
    else:
        label_img.configure(image=imagem_ref)
        label_img.image = imagem_ref
        label_img.place(relx=0.5, rely=0.75, anchor="center")

# Esconde a imagem
def esconder_imagem():
    if label_img:
        label_img.place_forget()

# Atualiza ao digitar
def ao_digitar(*args):
    if not entrada_texto.get():
        esconder_imagem()

entrada_texto.trace_add("write", ao_digitar)

# Alternar tema claro/escuro
def alternar_tema():
    global tema_atual
    novo = "darkly" if tema_atual == "flatly" else "flatly"
    salvar_tema(novo)
    style.theme_use(novo)
    tema_atual = novo

# ===== Layout =====
main_frame = tk.Frame(root, bg=style.colors.bg)
main_frame.pack(expand=True)

label = Label(main_frame, text="Gerador de Código QR", font=("Arial", 16))
input_entry = Entry(main_frame, textvariable=entrada_texto, font=("Arial", 12), width=40)
button = Button(main_frame, text="Gerar QR Code", command=qr_generator, bootstyle=PRIMARY)
toggle_button = Button(main_frame, text="Alternar Tema", command=alternar_tema, bootstyle=SECONDARY)
error_label = Label(main_frame, text="", font=("Arial", 10), foreground="red")

# Posicionamento
label.pack(pady=10)
input_entry.pack(pady=6)
button.pack(pady=4)
toggle_button.pack(pady=4)
error_label.pack(pady=6)

# Atalho Enter ↵
root.bind("<Return>", qr_generator)

root.mainloop()
