"""Ejercicio 3: sintaxis de órdenes y consultas SCPI."""
def es_consulta(comando):
    return isinstance(comando, str) and comando.endswith("?")

def validar(comando):
    if not isinstance(comando, str) or not comando.strip():
        return "Comando vacío"
    if not comando.startswith((":", "*")):
        return "Debe empezar con : o *"
    if "  " in comando:
        return "Hay espacios consecutivos"
    if comando.count("?") > 1:
        return "Hay más de un signo ?"
    if "?" in comando and not comando.endswith("?"):
        return "El signo ? debe ir al final"
    partes = comando.split(" ")
    if es_consulta(comando):
        if len(partes) != 1:
            return "Una consulta no lleva argumentos"
    elif len(partes) > 2 or (len(partes) == 2 and not partes[1]):
        return "Una orden admite un único argumento"
    return None

if __name__ == "__main__":
    assert es_consulta(":CH1:DISPlay?")
    assert not es_consulta(":CH1:DISPlay ON")
    assert validar(":CH1:SCALe 1v") is None
    assert validar("") is not None
    assert validar("CH1:DISPlay ON") is not None
    assert validar(":CH1:DISPlay??") is not None
    assert validar(":CH1:DISPlay ON?") is not None
    print("pruebas OK")
