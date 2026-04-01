def es_palindromo(palabra):
    # Normalizamos el texto: minúsculas y sin espacios
    texto_limpio = palabra.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]