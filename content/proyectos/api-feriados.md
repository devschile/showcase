+++
title = "Feriados API Chile"
date = "2025-11-24T00:00:00-03:00"
draft = false
description = "API REST que devuelve los feriados de Chile para un año dado."
tags = ["api", "open-source"]

[params]
category = "Open Source"
hero_image = "https://i.imgur.com/pFX0DLo.png"
contact_url = ""
project_url = "https://feriados.devschile.cl/"

[params.author]
name = "Jorge Epuñan H."
role = "Huemul Developer && Ex-best admin"
avatar = "https://avatars.githubusercontent.com/u/362186?s=400&u=4052131634180f584e7d3c3b156a7bc2d507b8fc&v=4"
quote = ""
github_url = "https://github.com/juanbrujo"
twitter_url = "https://x.com/csslab"
+++

# Endpoints

`https://feriados.devschile.cl/api/holidays/{year}`

# Formato de respuesta

```json
{
  "year": 2026,
  "feriados": {
  "enero": [
    {
      "mes": 1,
      "dia": 1,
      "dia_semana": "jueves",
      "descripcion": "Año Nuevo",
      "tipo": "civil",
      "irrenunciable": true
    }
  ],
  "abril": [
    {
      "mes": 4,
      "dia": 3,
      "dia_semana": "viernes",
      "descripcion": "Viernes Santo",
      "tipo": "religioso",
      "irrenunciable": false
    },
    ...
```

# Campos por feriado

- **mes**: número de mes (1-12)
- **dia**: día del mes
- **dia_semana**: nombre del día en español
- **descripcion**: texto breve
- **tipo**: civil o religioso
- **irrenunciable**: boolean
