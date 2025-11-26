from datetime import datetime
def padronizar_texto(texto):
    texto = texto.lower()
    texto = texto.strip()
    return texto
def data_valida(data_texto):
    try:
        datetime.strptime(data_texto, "%Y/%m/%d")
        return True
    except ValueError:
        return False