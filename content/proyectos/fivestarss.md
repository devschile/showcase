+++
title = "FivestaRSS"
author = "ivmirx"
owner_github = "qotoqot"
date = "2026-07-04T00:00:00-04:00"
draft = false
description = "Servicio self-hosted que convierte reseñas de App Store y Google Play en feeds RSS"
tags = ["rss", "app-store", "google-play", "open-source", "csharp", "dotnet"]

[params]
project_url = "https://github.com/QotoQot/FivestaRSS"
contact_url = "https://github.com/ivmirx"
category = "Open Source"
hero_image = "https://opengraph.githubassets.com/1/QotoQot/FivestaRSS"

[params.author]
name = "Ivan Mir"
role = "indie app developer"
avatar = "https://avatars.githubusercontent.com/u/10554114?v=4"
quote = "sabbe sattā sukhitā hontu"
contact_url = "https://qotoqot.com/contact/"
github_url = "https://github.com/ivmirx"
twitter_url = "https://x.com/ivmirx"
+++

## Descripción

FivestaRSS es una pequeña app self-hosted para monitorear reseñas de apps en App Store y Google Play, y publicarlas como feeds RSS 2.0 independientes para cada app.

El feed puede conectarse a Slack, Discord o cualquier lector y automatización compatible con RSS.

## Características

- Genera un feed RSS por app monitoreada.
- No usa base de datos: los archivos del feed son el almacenamiento persistente de las reseñas ya procesadas.
- Publica errores de APIs o servidor dentro del feed, para que los fallos del servicio también sean visibles.
- Permite configurar el intervalo de revisión de nuevas reseñas.

## Implementación

El proyecto está hecho en .NET y cuenta con licencia MIT. El repositorio incluye documentación para configurar las APIs, publicar el servicio y conectarlo con Discord o Slack a través de Zapier.
