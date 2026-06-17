from flask import Flask, render_template
import re
import socket

app = Flask(__name__)


HOST = "192.168.1.127"
PORT = 12345


VALOR_MINIMO = -10.0
VALOR_MAXIMO = 10.0
TAMANO_MATRIZ = 4


def leer_sensor():

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexion:
            conexion.settimeout(5)
            conexion.connect((HOST, PORT))

            contenido = conexion.recv(4096).decode(
                "utf-8",
                errors="ignore"
            )

        print("DATOS RECIBIDOS:")
        print(contenido)

        # Busca lecturas con el formato:
        # X:0.51,Y:2.03
        lecturas = re.findall(
            r"X:\s*([-+]?\d+(?:\.\d+)?)\s*,\s*Y:\s*([-+]?\d+(?:\.\d+)?)",
            contenido
        )

        if not lecturas:
            raise ValueError(
                "No se encontró una lectura válida con formato X:valor,Y:valor"
            )

        # Si llegan varias líneas en un mismo paquete, utiliza la última.
        valor_x, valor_y = lecturas[-1]

        eje_x = float(valor_x)
        eje_y = float(valor_y)

        print(f"LECTURA UTILIZADA: X={eje_x}, Y={eje_y}")

        return eje_x, eje_y, True

    except Exception as error:
        print("ERROR AL LEER LA APK:")
        print(type(error).__name__, "-", error)

        return 0.0, 0.0, False


def escalar(valor):
    """
    Convierte un valor entre -10 y 10 en una posición
    válida entre 0 y 3 para la matriz 4x4.
    """

    valor_limitado = max(
        VALOR_MINIMO,
        min(VALOR_MAXIMO, valor)
    )

    proporcion = (
        (valor_limitado - VALOR_MINIMO)
        / (VALOR_MAXIMO - VALOR_MINIMO)
    )

    posicion = int(proporcion * TAMANO_MATRIZ)

    return min(
        TAMANO_MATRIZ - 1,
        max(0, posicion)
    )


@app.route("/")
def index():
    eje_x, eje_y, conexion_correcta = leer_sensor()

    return render_template(
        "index.html",
        ejeX=eje_x,
        ejeY=eje_y,
        conexionCorrecta=conexion_correcta
    )


@app.route("/matrix")
def matrix():
    eje_x, eje_y, conexion_correcta = leer_sensor()

    posicion_x = escalar(eje_x)
    posicion_y = escalar(eje_y)

    return render_template(
        "matrix.html",
        ejeX=eje_x,
        ejeY=eje_y,
        x=posicion_x,
        y=posicion_y,
        conexionCorrecta=conexion_correcta
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True,
        use_reloader=False
    )
 
