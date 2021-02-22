from io import open
with open("index.html","w")as f:
    abrir = f.writelines("Datos\n")

    vhtml="""<!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <mta name="viewport" cont="width = device-width,initial-scale=1.0">
        <meta http-equiv="X-UA-Conpatible" content ="ie=edge">
        <title>Datos de archivo de entrada</title>
        <link rel="stylesheet" href="estilos.css">
        </head>
        <body>
        <p class="violeta">Metodos.py
        </p>

        </body>
        </html>
        """
    abrir=f.writelines(vhtml)
