# Contexto de BuildTrack para agentes

## Producto y alcance

BuildTrack es una API web para que BuildRight Contractors siga proyectos de renovación comercial. El MVP centraliza proyectos, hitos, tareas, incidencias y resúmenes semanales. No implementar presupuesto, compras, BIM, geolocalización avanzada, aplicación móvil nativa, autenticación ni persistencia mientras no se solicite expresamente.

## Estructura y convenciones

- `src/main.py`: aplicación FastAPI y rutas delgadas. Las rutas adaptan HTTP y delegan la lógica al servicio.
- `src/services/tracking_service.py`: reglas de negocio y acceso a los datos simulados.
- `src/data/mock_data.py`: datos temporales en memoria.
- `tests/`: pruebas con `unittest`; ejecutar `python -m unittest discover -s tests -v`.
- La API devuelve directamente los diccionarios de datos simulados. Para recursos inexistentes usar HTTP 404; para reglas de negocio incumplidas usar HTTP 400 con un mensaje claro.

## Slice 015 como referencia

El endpoint `PATCH /milestones/{milestone_id}/status` es el patrón de referencia para una actualización de estado:

1. El identificador del recurso va en la ruta y el nuevo estado en un modelo Pydantic.
2. La ruta de `main.py` delega al servicio y traduce `LookupError` a 404 y `ValueError` a 400.
3. El servicio valida las reglas antes de modificar los datos.
4. Las pruebas cubren el caso permitido y el caso rechazado.

## Segundo slice solicitado

Implementar la actualización de estado de una tarea siguiendo el patrón del Slice 015. Mantener los cambios dentro del alcance de la API en memoria y añadir pruebas automatizadas de éxito y recurso inexistente.
