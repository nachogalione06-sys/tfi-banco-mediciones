# Ejercicio 3 - Revisar si los comandos estan bien escritos


def es_consulta(comando):
    if not isinstance(comando, str):
        return False
    return comando.endswith("?")


def validar(comando):
    if not isinstance(comando, str) or comando.strip() == "":
        return "El comando esta vacio"

    if not comando.startswith(":") and not comando.startswith("*"):
        return "Tiene que empezar con : o *"

    if "  " in comando:
        return "Hay dos espacios seguidos"

    if comando.count("?") > 1:
        return "Hay mas de un signo de pregunta"

    if "?" in comando and not comando.endswith("?"):
        return "El signo de pregunta tiene que ir al final"

    partes = comando.split(" ")

    if es_consulta(comando):
        if len(partes) != 1:
            return "Las consultas no llevan argumentos"
    else:
        if len(partes) > 2 or (len(partes) == 2 and partes[1] == ""):
            return "La orden solo puede llevar un argumento"

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
