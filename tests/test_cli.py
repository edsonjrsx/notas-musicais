import pytest
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()

def test_escala_cli_deve_retornar_0_no_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 0

@pytest.mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_as_notas_na_resposta_de_do(nota):
    result = runner.invoke(app)
    assert nota in result.stdout

@pytest.mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_escala_cli_deve_conter_as_notas_na_resposta_de_fa(nota):
    result = runner.invoke(app, ['F', 'maior'])
    assert nota in result.stdout

@pytest.mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_todos_os_graus(grau):
    result = runner.invoke(app, ['F'])
    assert grau in result.stdout

