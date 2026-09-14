# Branch Protection para flujo CMS

## Objetivo

Permitir que la comunidad proponga cambios via PR desde CMS y que solo admins hagan merge a `main`.

## Requisitos previos

- Repositorio en GitHub con rama principal `main`.
- Workflow de ownership activo:
  - `.github/workflows/project-owner-guard.yml`

## Configuracion recomendada (GitHub)

1. Ir a `Settings` del repositorio.
2. Abrir `Branches`.
3. Crear o editar una branch rule para `main`.

Configurar:

1. `Require a pull request before merging`: ON.
2. `Require approvals`: ON (al menos 1).
3. `Require status checks to pass before merging`: ON.
4. Marcar como required check:
   - `validate-project-ownership` (job del workflow Project Owner Guard).
5. `Restrict who can push to matching branches`: ON (solo admins/mantenedores).
6. `Allow force pushes`: OFF.
7. `Allow deletions`: OFF.

## Restriccion de ownership

El workflow valida que cada PR cumpla:

1. Archivos nuevos en `content/proyectos/` deben incluir `owner_github`.
2. `owner_github` debe coincidir con `github.actor` del PR.
3. En archivos existentes no se puede cambiar el owner.
4. No se puede editar o borrar un proyecto de otro owner.

## Checklist de verificacion

1. Usuario A crea PR en su proyecto: debe pasar.
2. Usuario B edita proyecto de Usuario A: debe fallar.
3. Usuario B intenta cambiar `owner_github`: debe fallar.
4. Admin revisa y hace merge en `main`: debe funcionar.
