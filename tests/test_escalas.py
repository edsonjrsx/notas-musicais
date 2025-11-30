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
    ('tonica', 'tonalidade', 'esperado'), [
        ('C',  'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D',  'maior', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', 'maior', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E',  'maior', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F',  'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', 'maior', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G',  'maior', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', 'maior', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A',  'maior', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', 'maior', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B',  'maior', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
        ('C',  'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('D',  'menor', ['D', 'E', 'F', 'G', 'A', 'A#', 'C']),
        ('D#', 'menor', ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#']),
        ('E',  'menor', ['E', 'F#', 'G', 'A', 'B', 'C', 'D']),
        ('F',  'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
        ('F#', 'menor', ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']),
        ('G',  'menor', ['G', 'A', 'A#', 'C', 'D', 'D#', 'F']),
        ('G#', 'menor', ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#']),
        ('A',  'menor', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        ('A#', 'menor', ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#']),
        ('B',  'menor', ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']),
    ]
)
def test_deve_retornar_escala_correta(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)
    assert resultado['notas'] == esperado

def test_deve_retornar_graus_correto():
    tonica = 'C'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
