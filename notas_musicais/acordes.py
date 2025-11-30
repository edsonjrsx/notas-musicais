from notas_musicais.escalas import NOTAS_MUSICAIS, escala


def _menor(cifra):
    nota, _ = cifra.split('m')
    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo = 1)]
        graus = ['I', 'III-', 'V+']
    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']

    return notas, graus

def semitom(nota, *, intervalo):
    pos = NOTAS_MUSICAIS.index(nota) + intervalo
    return NOTAS_MUSICAIS[pos % 12]

def triade(nota, tonalidade):
    graus = (0, 2, 4)
    notas_da_escala, _ = escala(nota, tonalidade).values()

    return [notas_da_escala[grau] for grau in graus]

def acorde(cifra: str) -> dict[list[str], list[str]]:
    """
    Gera as notas de um acorde a partir de uma cifra.

    Parameters:
        cifra: Cifra do acorde (ex: 'C', 'Cm', 'Dº', 'E+', 'Fm+)

    Returns:
        Dicionário com notas e graus do acorde

    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

        >>> acorde('Cº')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}

        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}

        >>> acorde('Cm+')
        {'notas': ['C', 'D#', 'G#'], 'graus': ['I', 'III-', 'V+']}
    """
    graus = (0, 2, 4)
    if 'm' in cifra:
        notas, graus = _menor(cifra)
    elif 'º' in cifra:
        nota, _ = cifra.split('º')
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=-1)]
        graus = ['I', 'III-', 'V-']
    elif '+' in cifra:
        nota, _ = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ['I', 'III', 'V+']
    else:
        nota = cifra
        notas = triade(nota, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
