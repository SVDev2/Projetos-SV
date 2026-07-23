from PIL import Image

img = Image.open("static/imagens/fundo/logo.png")
img.save("favicon.ico")