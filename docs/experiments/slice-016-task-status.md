# Slice 016: actualización de estado de tareas

## Prompt breve aplicado

```text
Implementa la actualización de estado de una tarea siguiendo el patrón del Slice 015.
```

## Resultado

- Se añadió `PATCH /tasks/{task_id}/status`.
- La ruta delega la actualización al servicio y devuelve 404 para una tarea inexistente.
- Se añadieron pruebas de actualización y de recurso inexistente.
- La convención, estructura y comando de pruebas están documentados en `AGENTS.md`.
