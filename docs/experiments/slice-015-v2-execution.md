# Ejecución - Slice 015 - V2

## Prompt aplicado

```text
Actúa como desarrollador backend senior de BuildTrack. Implementa la regla de negocio: un hito no puede marcarse como completado si tiene tareas abiertas.

Objetivo: impedir que una actualización cambie el estado de un hito a "completed" cuando existan tareas asociadas cuyo estado no sea "completed".

El backend vive en src/. Usa src/main.py para las rutas, src/services/tracking_service.py para la lógica de negocio y src/data/mock_data.py para los datos simulados. Conserva la estructura actual y no agregues base de datos, autenticación, frontend ni dependencias nuevas. No modifiques documentación ni archivos fuera de src/.
```

## Implementación realizada

- Se añadieron tareas simuladas asociadas a hitos en `src/data/mock_data.py`.
- Se añadió `update_milestone_status` en `src/services/tracking_service.py` para centralizar la regla de negocio.
- Antes de actualizar un hito a `completed`, el servicio comprueba si tiene tareas asociadas con estado distinto de `completed`.
- Cuando existen tareas abiertas, el servicio devuelve un error y no cambia el estado del hito.
- Se añadió `PATCH /milestones/{milestone_id}/status` en `src/main.py`. Recibe un cuerpo JSON con el campo `status`.
- La ruta traduce un hito inexistente a HTTP 404 y una violación de la regla a HTTP 400.

## Validación realizada

- Se cargó la aplicación FastAPI y se confirmó que la ruta de actualización quedó registrada.
- Se verificó que un hito puede completarse cuando todas sus tareas están completadas.
- Se verificó que intentar completar un hito con una tarea abierta produce el error esperado.

## Nota del experimento

El prompt V2 restringía los cambios de implementación a `src/`. Este documento se añadió posteriormente por instrucción explícita del usuario para registrar el trabajo realizado; no forma parte de la implementación generada a partir del prompt único.
