NOTAS_MUSICAIS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica (str): A nota tônica da escala
        tonalidade (str): A tonalidade da escala

    Returns:
        Um dicionário contendo as notas e os graus da escala

    Raises:
        ValueError: Caso a tônica não seja válida
        KeyError: Caso a tonalidade não seja válida

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        tonica_pos = NOTAS_MUSICAIS.index(tonica)
        intervalos=ESCALAS[tonalidade]
    except ValueError:
        mensagem_erro = f"Essa nota não existe. Tente uma dessas: {', '.join(NOTAS_MUSICAIS)}"
        raise ValueError(mensagem_erro)
    except KeyError:
        mensagem_erro = ("Essa tonalidade não existe ou não foi implementada. "
                         f"Tente uma dessas: {', '.join(ESCALAS.keys())}")
        raise KeyError(mensagem_erro)

    tmp_array = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        tmp_array.append(NOTAS_MUSICAIS[nota])

    return {
        'notas': tmp_array,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
