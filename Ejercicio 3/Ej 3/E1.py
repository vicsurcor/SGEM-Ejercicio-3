from decimal import Decimal


def leerHorasMinSeg():

    r = 149, 30, 49

    return r


def segundos(h, m, s):

    s += (h * 3600) + (m * 60)

    return s


def importeLlamada(tiempo):

    coste = Decimal(input("Introduce el coste: "))

    return f"{tiempo * coste} € costará la llamada"


def horas(segundos):

    h = segundos // 3600
    segundos %= 3600
    m = segundos // 60
    segundos %= 60
    s = segundos

    return f"{h}, hora/s, {m}, minuto/s, {s}, segundo/s"
