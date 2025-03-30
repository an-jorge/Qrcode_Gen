import tkinter as tk
from PIL import Image, ImageTk

# Criar a janela principal
root = tk.Tk()
root.title("Qr_Generator")
root.geometry("600x400")

# Criar uma variável global para armazenar a imagem
imagem_ref = None 

 # funcao para gerar o QRCode 
def qr_generator():
    pass


# Função para exibir a imagem ao clicar no botão
def click():
    global imagem_ref  # Tornar a variável global para evitar ser apagada da memória

    imagem = Image.open("qr_code.png")  # Chamar a imagem
    imagem = imagem.resize((200, 200))  # Ajustar o tamanho da imagem
    imagem_ref = ImageTk.PhotoImage(imagem)  # Armazenar na variável global

    label_img = tk.Label(root, image=imagem_ref)
    label_img.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem

# Criar um rótulo e um botão
label = tk.Label(root, text="Hello World")
button = tk.Button(root, text="Clique em mim", command=click)

# Exibir na tela
label.pack(pady=20)
button.pack()

root.mainloop()
