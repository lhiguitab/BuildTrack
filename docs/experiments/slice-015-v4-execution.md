# Ejecución - Slice 015 - V4

## Prompt aplicado

Se ejecutó el prompt documentado para V4 en `docs/experiments/slice-015-v4.md`. La versión añade al prompt de V3 las convenciones reales de `src/main.py` y `src/services/tracking_service.py`.

## Implementación realizada

- `src/data/mock_data.py`: incorpora una tarea simulada asociada al hito existente.
- `src/services/tracking_service.py`: incorpora `update_milestone_status`. La función localiza el hito, valida la regla y realiza la actualización solamente si es válida.
- `src/main.py`: incorpora el modelo `MilestoneStatusUpdate` y una ruta delgada `PATCH /milestones/{milestone_id}/status` que delega al servicio.
- `tests/test_milestone_status.py`: incorpora pruebas automatizadas de los casos permitidos y del rechazo.

## Convenciones verificadas

- La ruta FastAPI contiene únicamente la adaptación de HTTP: recibe el cuerpo, delega en el servicio y traduce los errores a HTTP 400 o 404.
- La regla de negocio y el acceso a los datos simulados se mantienen en `tracking_service.py`.

## Criterios de aceptación verificados

1. La ruta `PATCH /milestones/{milestone_id}/status` permite solicitar la actualización.
2. El identificador se recibe por ruta y el estado en el cuerpo JSON.
3. Un estado distinto de `completed` se actualiza aunque haya tareas abiertas.
4. Se permite completar un hito sin tareas abiertas.
5. Se rechaza completar un hito con una tarea abierta.
6. El rechazo es HTTP 400 e incluye el mensaje `A milestone cannot be completed while it has open tasks`.
7. Los datos simulados contienen una tarea vinculada al hito.
8. Las pruebas cubren los dos escenarios de completado y el estado no final con tareas abiertas.

## Comando de pruebas ejecutado

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'; python -m unittest discover -s tests -v
```

Resultado: 3 pruebas ejecutadas y aprobadas.

## Nota del experimento

Este documento se añadió después de aplicar el prompt por instrucción explícita del usuario. El commit anterior contiene exclusivamente la implementación y las pruebas solicitadas por el prompt.
