import tkinter as tk
from ttkbootstrap import Label, Button, Entry
from ttkbootstrap.constants import PRIMARY, SECONDARY
from tkinter import messagebox
from PIL import ImageTk
from src.theme import salvar_tema
from src.qr_code_generator import gerar_qr_code

imagem_ref = None
label_img = None
entrada_texto = None


def criar_interface(root, style):
    global imagem_ref, label_img, entrada_texto
    entrada_texto = tk.StringVar()

    def exibir_imagem(imagem):
        global label_img
        imagem = imagem.resize((200, 200))
        imagem_ref = ImageTk.PhotoImage(imagem)

        if label_img is None:
            label_img = Label(root, image=imagem_ref)
            label_img.image = imagem_ref
            label_img.place(relx=0.5, rely=0.80, anchor="center")
        else:
            label_img.configure(image=imagem_ref)
            label_img.image = imagem_ref

    def esconder_imagem():
        if label_img:
            label_img.place_forget()

    def gerar_qr(event=None):
        texto = entrada_texto.get()
        if not texto:
            esconder_imagem()
            messagebox.showerror("Erro", "Texto não pode estar vázio!")
            return
        imagem = gerar_qr_code(texto)
        exibir_imagem(imagem)

    def alternar_tema():
        tema_atual = "darkly" if style.theme.name == "flatly" else "flatly"
        salvar_tema(tema_atual)
        style.theme_use(tema_atual)

    def ao_digitar(*args):
        # Verifica se o campo de texto está vazio e esconde a imagem
        if not entrada_texto.get():
            esconder_imagem()

    entrada_texto.trace_add("write", ao_digitar)

    main_frame = tk.Frame(root, bg=style.colors.bg)
    main_frame.pack(expand=True)

    label = Label(main_frame, text="Gerador de Código QR", font=("Arial", 16))
    input_entry = Entry(main_frame, textvariable=entrada_texto, font=("Arial", 15), width=40)
    button = Button(main_frame, text="Gerar QR Code", command=gerar_qr, bootstyle=PRIMARY)
    toggle_button = Button(main_frame, text="Alternar Tema", command=alternar_tema, bootstyle=SECONDARY)

    label.pack(pady=10)
    input_entry.pack(pady=6)
    button.pack(pady=4)
    toggle_button.pack(pady=4)

    root.bind("<Return>", gerar_qr)
