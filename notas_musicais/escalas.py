NOTAS_MUSICAIS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica (str): A nota tônica da escala
        tonalidade (str): A tonalidade da escala

    Returns:
        Um dicionário contendo as notas e os graus da escala

    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervalos=ESCALAS[tonalidade]
    tonica_pos = NOTAS_MUSICAIS.index(tonica)
    tmp_array = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        tmp_array.append(NOTAS_MUSICAIS[nota])

    return {
        'notas': tmp_array,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
