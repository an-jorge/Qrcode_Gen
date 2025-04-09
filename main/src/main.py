import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import qrcode.constants

# Criar a janela principal
root = tk.Tk()
root.title("Qr_Generator")
root.geometry("600x400")

# Variável global para a imagem e o widget da imagem
imagem_ref = None
label_img = None

# Variável de controle do campo de texto
entrada_texto = tk.StringVar()

# Função para gerar o QRCode 
def qr_generator():
    texto = entrada_texto.get()

    if not texto:
        error_label.config(text="O texto não pode estar vazio!", fg="red")
        esconder_imagem()
        return

    QR = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    QR.add_data(texto)
    QR.make(fit=True)

    img = QR.make_image(fill="black", back_color="white")
    img.save("qr_code.png")

    error_label.config(text="")
    exibir_imagem()

# Função para exibir a imagem
def exibir_imagem():
    global imagem_ref, label_img

    imagem = Image.open("qr_code.png")
    imagem = imagem.resize((200, 200))
    imagem_ref = ImageTk.PhotoImage(imagem)

    if label_img is None:
        label_img = tk.Label(root, image=imagem_ref)
        label_img.place(relx=0.5, rely=0.7, anchor="center")
    else:
        label_img.configure(image=imagem_ref)
        label_img.image = imagem_ref
        label_img.place(relx=0.5, rely=0.6, anchor="center")

# Função para esconder a imagem
def esconder_imagem():
    global label_img
    if label_img:
        label_img.place_forget()

# Função chamada sempre que o texto é alterado
def ao_digitar(*args):
    texto = entrada_texto.get()
    if not texto:
        esconder_imagem()

# Conectar a função de digitação à variável de entrada
entrada_texto.trace_add("write", ao_digitar)

# Criar rótulos, campo de entrada e botão
label = tk.Label(root, text="Gerar Codigo QR")
input_entry = tk.Entry(root, textvariable=entrada_texto)
button = tk.Button(root, text="Gerar Codigo QR", command=qr_generator)
error_label = tk.Label(root, text="", fg="red")

# Exibir na tela
label.pack(pady=20)
input_entry.pack(padx=7, pady=4)
button.pack()
error_label.pack(pady=10)

root.mainloop()
