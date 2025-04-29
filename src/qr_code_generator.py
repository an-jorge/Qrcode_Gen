# --- qr_code_generator.py ---
import os
import qrcode
from PIL import Image

def gerar_qr_code(texto, output="qr_code.png"):

      # Verifica se a pasta 'assets' existe, se não, cria
    os.makedirs('assets', exist_ok=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("assets/qr_code.png")
    return Image.open("assets/qr_code.png")


