# Experimento de prompts - Slice 015 - V2

## Propósito

Evaluar el resultado al añadir rol, objetivo y restricciones al prompt base.

## Slice

Un hito no puede marcarse como completado si tiene tareas abiertas.

## Prompt único

```text
Actúa como desarrollador backend senior de BuildTrack. Implementa la regla de negocio: un hito no puede marcarse como completado si tiene tareas abiertas.

Objetivo: impedir que una actualización cambie el estado de un hito a "completed" cuando existan tareas asociadas cuyo estado no sea "completed".

El backend vive en src/. Usa src/main.py para las rutas, src/services/tracking_service.py para la lógica de negocio y src/data/mock_data.py para los datos simulados. Conserva la estructura actual y no agregues base de datos, autenticación, frontend ni dependencias nuevas. No modifiques documentación ni archivos fuera de src/.
```

## Restricción del experimento

Aplicar únicamente el prompt anterior en esta rama. No complementar el pedido con información adicional durante la implementación.

## Evaluación posterior

Calificar el resultado sobre los mismos 8 criterios comunes de V1, V3 y V4. Registrar el puntaje y las observaciones al finalizar la ejecución.
