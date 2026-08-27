# Experimento de prompts - Slice 015 - V3

## Propósito

Evaluar el resultado al añadir criterios de aceptación y formato de entrega al prompt de V2.

## Slice

Un hito no puede marcarse como completado si tiene tareas abiertas.

## Prompt único

```text
Actúa como desarrollador backend senior de BuildTrack. Implementa la regla de negocio: un hito no puede marcarse como completado si tiene tareas abiertas.

Objetivo: impedir que una actualización cambie el estado de un hito a "completed" cuando existan tareas asociadas cuyo estado no sea "completed".

El backend vive en src/. Usa src/main.py para las rutas, src/services/tracking_service.py para la lógica de negocio y src/data/mock_data.py para los datos simulados. Conserva la estructura actual y no agregues base de datos, autenticación, frontend ni dependencias nuevas. No modifiques documentación ni archivos fuera de src/.

Criterios de aceptación:
1. Existe una forma HTTP de solicitar la actualización de estado de un hito.
2. La actualización recibe el identificador del hito y el nuevo estado.
3. Si el nuevo estado no es "completed", la actualización se permite.
4. Si el nuevo estado es "completed" y no hay tareas abiertas, la actualización se permite.
5. Si el nuevo estado es "completed" y existe al menos una tarea asociada no completada, la actualización se rechaza.
6. El rechazo responde con HTTP 400 e indica claramente que hay tareas abiertas.
7. Los datos simulados incluyen tareas asociadas a hitos para poder ejercer ambos escenarios.
8. Incluye pruebas automatizadas de éxito y rechazo, y deben pasar.

Formato de entrega: implementa los cambios directamente en el repositorio. Al finalizar, indica los archivos modificados y el comando de pruebas ejecutado.
```

## Restricción del experimento

Aplicar únicamente el prompt anterior en esta rama. No complementar el pedido con información adicional durante la implementación.

## Evaluación posterior

Calificar el resultado sobre los 8 criterios enumerados. Registrar el puntaje y las observaciones al finalizar la ejecución.
