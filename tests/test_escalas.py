import re

import pytest

from notas_musicais.escalas import ESCALAS, NOTAS_MUSICAIS, escala


def test_deve_funcionar_com_notas_minuscalas():
    tonica = 'c'
    tonalidade = 'maior'

    result = escala(tonica, tonalidade)

    assert result

def test_deve_retornar_erro_quando_a_nota_nao_existe():
    tonica = 'Y'
    tonalidade = 'maior'

    mensagem_erro = f"Essa nota não existe. Tente uma dessas: {', '.join(NOTAS_MUSICAIS)}"

    with pytest.raises(ValueError, match=re.escape(mensagem_erro)) as error:
        escala(tonica, tonalidade)

    assert error.value.args[0] == mensagem_erro

def test_deve_retornar_erro_quando_a_escala_nao_existe():
    tonica = 'C'
    tonalidade = 'desconhecida'

    mensagem_erro = ("Essa tonalidade não existe ou não foi implementada. "
                     f"Tente uma dessas: {', '.join(ESCALAS.keys())}")

    with pytest.raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert error.value.args[0] == mensagem_erro

@pytest.mark.parametrize(
    ('tonica', 'esperado'), [
        ('C',  ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D',  ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E',  ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F',  ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G',  ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A',  ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B',  ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
    ]
)
def test_deve_retornar_escala_correta(tonica, esperado):
    tonalidade = 'maior'
    resultado = escala(tonica, tonalidade)
    assert resultado['notas'] == esperado

def test_deve_retornar_graus_correto():
    tonica = 'C'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
