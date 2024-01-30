
def leerHorasMinSeg():

    h = int(input("Introduce las horas: "))
    m = int(input("Introduce los minutos: "))
    s = int(input("Introduce los segundos: "))

    return f"{h} hora/s", f" {m} minuto/s", f" {s} segundo/s"


def segundos(h, m, s):

    return f"{h * 3600} + {m * 60} + {s}  segundo/s"


def importeLlamada(tiempo, coste):

    return f"{tiempo * coste}  € costará la llamada"


def horas(segundos):

    h = segundos // 3600
    segundos %= 3600
    m = segundos // 60
    segundos %= 60
    s = segundos

    return f"{h}, hora/s, {m}, minuto/s, {s}, segundo/s"

print(segundos())
print(importeLlamada())
print(horas())