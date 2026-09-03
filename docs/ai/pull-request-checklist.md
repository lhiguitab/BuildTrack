# Descripción y checklist del pull request - Lab 03

## Título

`docs: entregar evidencias del Lab 03`

## Descripción

Este pull request entrega las evidencias del Lab 03. La mejor implementación del primer slice corresponde a V4 y fue integrada previamente a `main` mediante el commit de fusión `569df97`. Esta rama añade la evaluación, plantillas reutilizables y declaración de uso de IA que documentan dicha selección.

## Checklist de verificación

- [x] La implementación V4 del Slice 015 está integrada en `main`.
- [x] La regla impide completar un hito con tareas abiertas y devuelve HTTP 400.
- [x] La ruta delega la regla de negocio al servicio.
- [x] El segundo slice incorpora `PATCH /tasks/{task_id}/status`.
- [x] `AGENTS.md` está en la raíz con el contexto reutilizable del proyecto.
- [x] `docs/ai/escalera-lab03.md` contiene las cuatro versiones, puntajes, alucinaciones y conclusión.
- [x] `docs/ai/prompts/` contiene tres plantillas reutilizables.
- [x] `docs/ai/uso-ia.md` declara el uso de herramientas y modelos conocido.
- [x] `python -m unittest discover -s tests -v` pasa: 5 pruebas aprobadas.
