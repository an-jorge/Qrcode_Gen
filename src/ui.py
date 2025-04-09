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
        global label_img, imagem_ref

        imagem = imagem.resize((200, 200))
        imagem_ref = ImageTk.PhotoImage(imagem)

        if label_img is None:
            label_img = Label(root, image=imagem_ref)
            label_img.image = imagem_ref
            label_img.place(relx=0.5, rely=0.79, anchor="center")
        else:
            label_img.configure(image=imagem_ref)
            label_img.image = imagem_ref
            label_img.place(relx=0.5, rely=0.79, anchor="center")

    def esconder_imagem():
        global label_img
        if label_img:
            label_img.place_forget()  # Remove a imagem
            label_img = None  # Limpa a referência

    def gerar_qr(event=None):
        texto = entrada_texto.get()
        if not texto:
            esconder_imagem()  # Remove a imagem caso o campo esteja vazio
            messagebox.showerror("Erro", "O texto não pode estar vázio!")
            return

        imagem = gerar_qr_code(texto)
        esconder_imagem()  # Esconde a imagem anterior antes de exibir a nova
        exibir_imagem(imagem)

    def alternar_tema():
        tema_atual = "darkly" if style.theme.name == "flatly" else "flatly"
        salvar_tema(tema_atual)
        style.theme_use(tema_atual)

    def ao_digitar(*args):
        texto = entrada_texto.get()
        if not texto:
            esconder_imagem()  # Esconde a imagem quando o texto for apagado

    # Monitorar o campo de texto para esconder a imagem
    entrada_texto.trace_add("write", ao_digitar)

    main_frame = tk.Frame(root, bg=style.colors.bg)
    main_frame.pack(expand=True)

    label = Label(main_frame, text="Gerador de Código QR", font=("Arial", 16))
    input_entry = Entry(main_frame, textvariable=entrada_texto, font=("Arial", 16), width=40)
    button = Button(main_frame, text="Gerar QR Code", command=gerar_qr, bootstyle=PRIMARY)
    toggle_button = Button(main_frame, text="Alternar Tema", command=alternar_tema, bootstyle=SECONDARY)

    label.pack(pady=10)
    input_entry.pack(pady=6)
    button.pack(pady=4)
    toggle_button.pack(pady=4)

    root.bind("<Return>", gerar_qr)
