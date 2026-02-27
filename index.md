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

<ul class="projects-grid">
{% for p in site.projects %}
	<li class="project-card" role="button" tabindex="0"
			data-title="{{ p.title | escape }}"
			data-author="{{ p.author | default: '' | escape }}"
			data-repo="{{ p.repo | default: '' | escape }}"
			data-tech="{{ p.tech | default: '' | escape }}">
		<h3>{{ p.title }}</h3>
		<div class="project-meta">{{ p.author }} {% if p.tech %}• {{ p.tech }}{% endif %}</div>
		<div class="project-summary">{{ p.description }}</div>
		<div class="project-actions"><a href="#" class="open-detail">Ver detalle</a></div>
		<div class="project-full" style="display:none">
			<p><strong>Tipo:</strong> {{ p.type }}</p>
			{% if p.demo %}<p><strong>Demo:</strong> <a href="{{ p.demo }}" target="_blank">{{ p.demo }}</a></p>{% endif %}
			<div class="project-content">{{ p.content | markdownify }}</div>
		</div>
	</li>
{% endfor %}
</ul>
