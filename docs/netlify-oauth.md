# Netlify OAuth para Decap CMS

## Objetivo

Habilitar login con GitHub en `/admin/` usando el OAuth Provider nativo de Netlify.

## Requisitos previos

- Sitio desplegado en Netlify.
- GitHub OAuth App creada.
- Decap CMS configurado en `static/admin/config.yml`.

## Configuracion en GitHub

1. Ir a GitHub > Settings > Developer settings > OAuth Apps.
2. Abrir (o crear) la OAuth App del proyecto.
3. Configurar `Authorization callback URL` con:

```text
https://api.netlify.com/auth/done
```

4. Guardar cambios y copiar:
- `Client ID`
- `Client Secret`

## Configuracion en Netlify

1. Ir a `Project configuration`.
2. Abrir `Access & security`.
3. Entrar a `OAuth`.
4. En `Authentication Providers`, elegir `Install Provider`.
5. Seleccionar `GitHub`.
6. Pegar `Client ID` y `Client Secret`.
7. Guardar.

## Validacion

1. Ir a `https://<tu-dominio>/admin/`.
2. Iniciar sesion con GitHub.
3. Verificar que Decap permite crear/editar contenido y generar PR.

## Scope de autorizacion

El backend `github` de Decap solicita el scope declarado en `auth_scope` (`static/admin/config.yml`). Se usa `public_repo` (no `repo`) porque `devschile/showcase` es un repositorio publico:

- `repo`: control total, incluye repositorios privados. Innecesario aqui y genera una pantalla de consentimiento mas invasiva para quien va a publicar.
- `public_repo`: acceso solo a repositorios publicos. Suficiente para que Decap haga fork (open_authoring) y cree ramas/PRs.

No requiere crear ni reconfigurar la OAuth App en GitHub: el scope no es un ajuste de la app, lo pide el cliente (Decap) en cada login.

Colaboradores que ya autorizaron la app con el scope `repo` anterior mantienen ese grant amplio hasta que lo revoquen manualmente:

1. Ir a `https://github.com/settings/applications` > pestana "Authorized OAuth Apps".
2. Buscar la app usada por Netlify OAuth y click en `Revoke`.
3. Volver a `/admin/` e iniciar sesion de nuevo para recibir el consentimiento reducido.

## Troubleshooting rapido

- Error de callback: revisar URL exacta `https://api.netlify.com/auth/done`.
- Login no inicia: confirmar provider GitHub instalado en Netlify.
- Token invalido: regenerar Client Secret y actualizar en Netlify.
- Error al guardar con `API_ERROR` y mensaje de `OAuth App access restrictions`:
	- Causa: la organizacion GitHub (`devschile`) tiene restringido el acceso de OAuth Apps de terceros.
	- Solucion (requiere owner de la org):
		1. Ir a GitHub > `devschile` > Settings > Third-party access.
		2. Buscar la OAuth App usada por Netlify OAuth (la app con tu `Client ID`).
		3. Aprobar acceso para la organizacion.
		4. Reintentar guardar desde `/admin/`.
	- Alternativa: desactivar temporalmente esa restriccion en la organizacion (menos recomendado).
