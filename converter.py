from PIL import Image

#Procedemos a cargar la imagen web
imagen_webp = Image.open('icy_planet.webp')

#Ahora se procede a guardar la imagen en formato png
imagen_webp.save('icy_planet2.png')

