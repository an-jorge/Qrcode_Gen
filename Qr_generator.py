import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import qrcode.console_scripts
import qrcode.constants

# Criar a janela principal
root = tk.Tk()
root.title("Qr_Generator")
root.geometry("600x400")

# Criar uma variável global para armazenar a imagem
imagem_ref = None 

 # funcao para gerar o QRCode 
def qr_generator():

    texto = input.get()

    # Gerar codigo QR
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

    click()        


# Função para exibir a imagem ao clicar no botão
def click():
    global imagem_ref  # Tornar a variável global para evitar ser apagada da memória

    imagem = Image.open("qr_code.png")  # Chamar a imagem
    imagem = imagem.resize((200, 200))  # Ajustar o tamanho da imagem
    imagem_ref = ImageTk.PhotoImage(imagem)  # Armazenar na variável global

    label_img = tk.Label(root, image=imagem_ref)
    label_img.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem

# Criar um rótulo e um botão
label = tk.Label(root, text="Gerar Codigo QR")
input = tk.Entry(root)
button = tk.Button(root, text="Gerar Codigo QR", command=qr_generator)

# Exibir na tela
label.pack(pady=20)
input.pack(padx=7, pady=4)
button.pack()

root.mainloop()
