import os
from tkinter.filedialog import askdirectory

#.doc, .pptx, .jpg, .png, .pdf, .xlsx, .docx, .txt

caminho = askdirectory(title="Selecione a pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", "jpg"],
    "planilhas": ["xlsx"],
    "pdfs": [".pdf"],
    "documentos": [".doc", ".docx"],
    "textos": [".txt"],
    "slides": [".pptx"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")