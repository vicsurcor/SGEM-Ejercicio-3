def telegrama(texto, costeCorta, costeLarga):
    palabras = texto.split()
    costeTotal = 0
    telegrama = []

    for palabra in palabras:

        if len(palabra) > 5:

            if palabra.endswith('.'):
                palabra = palabra[:5] + "@"
                costeTotal += costeLarga
                telegrama.append(palabra)
                telegrama.append('STOP')

            elif palabra.endswith('.  '):
                palabra = palabra[:5] + "@"
                costeTotal += costeLarga
                telegrama.append(palabra)
                telegrama.append('STOPSTOP')

            else:
                palabra = palabra[:5] + "@"
                telegrama.append(palabra)
                costeTotal += costeLarga

        else:
            costeTotal += costeCorta
            telegrama.append(palabra)

            if palabra.endswith('.'):
                costeTotal += costeCorta
                telegrama.append(palabra)
                telegrama.append('STOP')

            elif palabra.endswith('.  '):
                costeTotal += costeCorta
                telegrama.append(palabra)
                telegrama.append('STOPSTOP')

    return ' '.join(telegrama), costeTotal


texto = "fdureoihgoer fuibwebu. jfds ifewowieio."
costeCorta = 10
costeLarga = 20

textoTelegrama, coste = telegrama(texto, costeCorta, costeLarga)


print(f"Telegrama: {textoTelegrama}")
print(f"Coste: {coste} céntimos")
print("Victor Suros")


