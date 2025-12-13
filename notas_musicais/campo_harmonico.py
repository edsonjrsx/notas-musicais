from notas_musicais.acordes import triade
from notas_musicais.escalas import escala


def _converte_graus (cifra: str, grau: str) -> str:
    """Converte graus numéricos em graus com notação romana.

    Parameters:
        cifra (str): A cifra do acorde.
        grau (str): O grau bruto a ser convertido.

    Returns:
        O grau em notação romana correspondente ao grau numérico.

    Examples:
        >>> _converte_graus('C', 'I')
        'I'

        >>> _converte_graus('Dm', 'II')
        'ii'
    """
    if cifra.endswith('m'):
        return grau.lower()
    elif cifra.endswith('º'):
        return grau.lower() + 'º'
    else:
        return grau

def _triade_na_escala (nota: str, notas_da_escala:list[str]) -> str:
    """Gera a tríade para uma determinada nota dentro de uma escala.

    Parameters:
        nota (str): A nota para a qual a tríade será gerada.

    Returns:
        A tríade correspondente à nota na escala.

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'

        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
    """
    tonica, terca, quinta = triade(nota, 'maior')

    match terca in notas_da_escala, quinta in notas_da_escala:
        case True, True:
            return f"{nota.upper()}"
        case False, True:
            return f"{nota.upper()}m"
        case False, False:
            return f"{nota.upper()}º"

def campo_harmonico(tonica: str, tocanlidade: str) -> dict[str, list[str]]:
    """
    Gera o campo harmônico para uma determinada tônica e tonalidade (maior ou menor).

    Parameters:
        tonica (str): A tônica da escala. Ex: 'C', 'D#' etc.
        tocanlidade (str): A tonalidade da escala. Ex: 'maior', 'menor' etc.

    Returns:
        Um campo harmônico representado como um dicionário com duas chaves:
        - 'acordes': Uma lista de acordes correspondentes a cada grau da escala.
        - 'graus': Uma lista de graus correspondentes a cada acorde.

    Examples:
        >>> campo_harmonico('C', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bº'], 'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viiº']}

        >>> campo_harmonico('C', 'menor')
        {'acordes': ['Cm', 'Dº', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'graus': ['i', 'iiº', 'III', 'iv', 'v', 'VI', 'VII']}
    """
    notas, _graus = escala(tonica, tocanlidade).values()
    acordes = [_triade_na_escala(nota, notas) for nota in notas]
    graus = [_converte_graus(acorde, grau) for acorde, grau in zip(acordes, _graus)]

    return {'acordes': acordes, 'graus': graus}
