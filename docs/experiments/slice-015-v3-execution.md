# Ejecución - Slice 015 - V3

## Prompt aplicado

Se ejecutó el prompt documentado para V3 en `docs/experiments/slice-015-v3.md`, incluyendo sus ocho criterios de aceptación.

## Cambios realizados

- `src/data/mock_data.py`: incorpora tareas simuladas vinculadas a un hito.
- `src/services/tracking_service.py`: incorpora la actualización de estado y bloquea la transición a `completed` cuando existe una tarea abierta.
- `src/main.py`: incorpora `PATCH /milestones/{milestone_id}/status`, con un cuerpo JSON que contiene `status`.
- `tests/test_milestone_status.py`: incorpora pruebas automatizadas de la transición permitida y del rechazo HTTP 400.

## Criterios de aceptación verificados

1. La ruta HTTP `PATCH /milestones/{milestone_id}/status` permite solicitar la actualización.
2. La ruta recibe el identificador como parámetro de ruta y el nuevo estado en el cuerpo.
3. Los estados distintos de `completed` no activan la restricción.
4. Se permite completar el hito si todas sus tareas están completadas.
5. Se rechaza completar el hito si una tarea asociada está abierta.
6. La ruta traduce el rechazo a HTTP 400 con el mensaje `A milestone cannot be completed while it has open tasks`.
7. Los datos simulados incluyen una tarea asociada para ambos escenarios.
8. Las pruebas automatizadas cubren éxito y rechazo.

## Comando de pruebas ejecutado

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'; python -m unittest discover -s tests -v
```

Resultado: 2 pruebas ejecutadas y aprobadas.

## Nota del experimento

El documento se añadió después de aplicar el prompt por instrucción explícita del usuario. Así, el commit de implementación conserva los cambios generados por el prompt y este commit registra la ejecución.
