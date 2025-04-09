
# --- theme.py ---
import json
import os

CONFIG_PATH = "config.json"

def carregar_tema_salvo():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as file:
            dados = json.load(file)
            return dados.get("tema", "flatly")
    return "flatly"

def salvar_tema(tema):
    with open(CONFIG_PATH, "w") as file:
        json.dump({"tema": tema}, file)

