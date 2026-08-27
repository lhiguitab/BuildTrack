# Ejecución - Slice 015 - V1

## Prompt aplicado

```text
Implementa la regla: un hito no puede marcarse como completado si tiene tareas abiertas.
```

## Implementación realizada

- Se añadieron tareas simuladas asociadas a hitos en `src/data/mock_data.py`.
- Se añadió `update_milestone_status` en `src/services/tracking_service.py`.
- Antes de cambiar un hito a `completed`, el servicio verifica que no haya tareas del mismo hito con estado distinto de `completed`.
- Cuando existen tareas abiertas, el servicio conserva el estado previo del hito y produce un error explicativo.
- Se añadió `PATCH /milestones/{milestone_id}/status` en `src/main.py`. Recibe un cuerpo JSON con `status`.
- La ruta devuelve HTTP 400 para la regla de negocio y HTTP 404 cuando el hito no existe.
- Se añadieron pruebas unitarias para el escenario permitido y el escenario bloqueado.

## Validación

Ejecutar desde la raíz del repositorio:

```powershell
python -m unittest discover -s tests -v
```

## Alcance no implementado

La solución usa los datos simulados existentes. No añade persistencia, autenticación, interfaz de usuario ni una entidad de tareas completa.
