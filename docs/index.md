![logo_projeto](assets/logo.png){ width="200" .center }

# Notas Musicais

Notas musicais é um  CLI para ajudar na formação de escalas musicais, acordes, campos harmônicos.

Todo a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando é o ponto de entrada para o CLI e será usado para chamar os subcomandos.

Temos três subcomandos principais: 'escala', 'acorde' e 'campo-harmonico'.

## Como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala
```

Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tônica na escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir.
Desta forma, você pode alterar a escala retornada. Por exemplo a escala de `F#`:

```bash
poetry run notas-musicais escala F#     
```

Resultando em:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Alteração na tonalidade da escala

Você pode alterar a tonalidade da escala também!
Esse é o segundo parâmetro da linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala D menor
```

Resultando em:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ D │ E  │ F   │ G  │ A │ A# │ C   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

## Acordes

Uso básico do comando acorde:

```bash
poetry run notas-musicais acorde C
```

Retornando os graus e as notas correspondentes a esse acorde:

```bash
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variações na cifra

```bash
poetry run notas-musicais acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento você pode usar acordes maiores (Ex: C), menores (Ex: Cm), aumentados (Ex: C+), diminutos (Ex: Cº), menores diminutos (Ex: Cmº);

## Campo Harmônico

Uso básico do comando campo-harmonico:

```bash
poetry run notas-musicais campo-harmonico [TONICA] [TONALIDADE]
```

Retornando os graus e as notas correspondentes a esse campo harmônico:

```bash
-> poetry run notas-musicais campo-harmonico
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ viiº ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ Bº   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica 'C' e o campo harmônico 'maior'.

### Alteração da tônica no campo harmônico

Você pode alterar a tônica do campo harmônico passando o primeiro parâmetro, . Por exemplo:

```bash
poetry run notas-musicais campo-harmonico D
```

Resultando em:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ viiº ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ D │ Em │ F#m │ G  │ A │ Bm │ C#º  │
└───┴────┴─────┴────┴───┴────┴──────┘
```

### Alteração na tonalidade do campo harmônico

Você pode alterar a tonalidade do campo harmônico passando o segundo parâmetro. Por exemplo:

```bash
poetry run notas-musicais campo-harmonico A menor
```

Resultando em:

```bash
┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ iiº ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Am │ Bº  │ C   │ Dm │ Em │ F  │ G   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag '--help':

```bash
poetry run escalas --help
```

Resultando em:

```bash
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...                                                                                                                                      

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                       │
│ --help                        Show this message and exit.                                                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ escala                                                                                                                                                                               │
│ acorde                                                                                                                                                                               │
│ campo-harmonico                                                                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
