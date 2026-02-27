---
layout: default
title: "devsChile ShowCase"
description: "Vitrina de proyectos de la comunidad devsChile"
---

# devsChile ShowCase()

> Vitrina de proyectos open-source y/o propietarios creados por colaboradores de la comunidad Slack devsChile.

Esta página actúa como entrada principal para que los miembros muestren sus proyectos.

## ¿Qué es esto?

`devsChile ShowCase()` es un sitio colectivo donde miembros de la comunidad pueden publicar breves fichas de sus proyectos (bibliotecas, herramientas, apps, demos, y más).

## Cómo añadir tu proyecto

Envía un Pull Request con una entrada en este mismo archivo siguiendo la plantilla de abajo, o crea un archivo Markdown individual por proyecto si prefieres (ej. `_projects/mi-proyecto.md`).

### Plantilla de proyecto (ejemplo)

```
### Nombre del Proyecto

- **Autor:** Pedro Pérez (@usuario)
- **Repositorio:** https://github.com/usuario/nombre-del-proyecto
- **Tipo:** Open-source / Propietario
- **Tecnologías:** React, Node.js, PostgreSQL
- **Descripción:** Una frase que explique el proyecto en 1-2 líneas.
- **Demo:** https://demo.example.com (opcional)

Breve explicación adicional o notas sobre cómo contribuir.
```

## Buenas prácticas

- Mantén la descripción corta y clara.
- Indica la licencia si es open-source.
- Añade etiquetas de tecnologías para facilitar la búsqueda.

## Licencia y derechos

Respeta la licencia del repositorio que enlazas. Para proyectos propietarios indica claramente que es privado y qué información puede compartirse públicamente.

## Proyectos

{% for p in site.projects %}
### {% if p.url %}[{{ p.title }}]({{ p.url }}){% else %}[{{ p.title }}](/projects/{{ p.title | slugify }}/){% endif %}

- **Autor:** {{ p.author }}
- **Repositorio:** {{ p.repo }}
- **Tipo:** {{ p.type }}
- **Tecnologías:** {{ p.tech }}
- **Descripción:** {{ p.description }}
{% if p.demo %}- **Demo:** {{ p.demo }}{% endif %}

{% endfor %}
