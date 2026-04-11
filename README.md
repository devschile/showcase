# `ShowCase()`

*por devsChile*

Portafolio comunitario de proyectos open-source y emprendimientos de la comunidad [devsChile](https://devschile.cl).

🔗 **https://showcase.devschile.cl**

---

## Cómo publicar tu proyecto

Hay dos formas: usando el CMS o directamente via Git.

### Opción A — CMS (recomendada, sin conocer Git)

1. Ve a [showcase.devschile.cl/admin/](https://showcase.devschile.cl/admin/) e inicia sesión con tu cuenta de GitHub.
2. Crea un nuevo proyecto en la colección **Proyectos**.
3. Completa los campos y guarda. Se abrirá un Pull Request automáticamente.
4. Un mantenedor revisará y publicará tu proyecto.

### Opción B — Pull Request manual

1. Haz fork del repositorio.
2. Crea una rama: `git checkout -b proyecto/nombre-de-tu-proyecto`.
3. Agrega tu archivo en `content/proyectos/nombre-de-tu-proyecto.md` (ver plantilla abajo).
4. Abre un Pull Request describiendo brevemente tu proyecto.
5. Un mantenedor revisará y publicará tu proyecto.

---

## Plantilla de proyecto

Crea `content/proyectos/nombre-de-tu-proyecto.md` con este contenido:

```toml
+++
title        = "Nombre de tu proyecto"
owner_github = "tu-usuario-github"
date         = "2026-01-01T00:00:00-03:00"
draft        = true
description  = "Una línea describiendo qué hace el proyecto."
tags         = ["Tag1", "Tag2"]

[params]
category    = "Open Source"
hero_image  = "https://placehold.co/1600x900/0f172a/94a3b8?text=Mi+Proyecto"
project_url = "https://github.com/tu-usuario/tu-proyecto"

[params.author]
name        = "Tu Nombre"
role        = "Frontend Developer"
avatar      = "https://github.com/tu-usuario.png"
quote       = "Una frase tuya."
contact_url = "mailto:tu@email.com"
github_url  = "https://github.com/tu-usuario"
twitter_url = "https://twitter.com/tu-usuario"
+++

## Descripción

Explica qué hace tu proyecto.

## Implementación

Tecnologías usadas, decisiones de arquitectura, etc.
```

### Campos obligatorios

| Campo | Descripción |
|---|---|
| `title` | Nombre del proyecto |
| `owner_github` | Tu username de GitHub (sin @) |
| `date` | Fecha en formato ISO 8601 |
| `description` | Bajada corta (máx ~160 caracteres) |

### Imágenes

- `hero_image`: **1600×900px** (relación 16:9).
- `avatar`: **256×256px** (cuadrado).
- Usa imágenes propias o libres de derechos. Placeholder temporal: `https://placehold.co/1600x900`.

---

## ¿Dudas?

Únete al [Slack de devsChile](https://devschile.cl). Juntos hacemos mejor comunidad.
