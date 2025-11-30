import pytest

from notas_musicais.acordes import acorde


@pytest.mark.parametrize(('nota', 'esperado'),
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('Cº', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#'])
    ]
)
def test_acorde_deve_retornar_as_notas_correspodentes(nota, esperado):
    notas, _ = acorde(nota).values()
    assert esperado == notas

@pytest.mark.parametrize(('cifra', 'esperado'),
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('Cº', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+',['I', 'III-', 'V+'])
    ]
)
def test_acorde_deve_retornar_os_graus_correspodentes(cifra, esperado):
    _, graus = acorde(cifra).values()
    assert esperado == graus

