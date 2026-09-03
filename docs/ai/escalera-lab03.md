# Lab 03 - Escalera de prompts

## Slice evaluado

**Regla de negocio:** un hito no puede marcarse como completado si tiene tareas abiertas.

## Versiones del prompt

| Versión | Prompt | Puntaje /8 | Alucinaciones |
| --- | --- | ---: | ---: |
| V1 | `Implementa la regla: un hito no puede marcarse como completado si tiene tareas abiertas.` | 5 | 0 |
| V2 | Añade rol backend, objetivo, rutas esperadas y restricción de no añadir dependencias ni componentes fuera de `src/`. | 4 | 0 |
| V3 | Añade los ocho criterios de aceptación y el formato de entrega. | 5 | 0 |
| V4 | Añade las convenciones reales de `src/main.py` y `src/services/tracking_service.py`. | 5 | 0 |

## Verificación binaria

| Criterio | V1 | V2 | V3 | V4 |
| --- | --- | --- | --- | --- |
| 1. Arranque con un solo comando documentado | No | No | No | No |
| 2. Ruta según convención REST declarada | No | No | No | No |
| 3. Regla de negocio del RFP | Sí | Sí | Sí | Sí |
| 4. Entrada validada y error estructurado | Sí | Sí | Sí | Sí |
| 5. Estructura y nombres de referencia | Sí | Sí | Sí | Sí |
| 6. Formato de respuesta de referencia | Sí | Sí | Sí | Sí |
| 7. Prueba de regla de negocio | Sí | No | Sí | Sí |
| 8. Dependencias declaradas en manifiesto | No | No | No | No |

Las alucinaciones se cuentan aparte. No se detectaron dependencias, campos, endpoints o archivos ajenos al alcance del RFP: la ruta, las tareas simuladas y las pruebas son necesarios para implementar o verificar el slice.

## Conclusión

Las cuatro versiones implementaron la regla central y respetaron el diseño existente de FastAPI, pero V2 perdió el criterio de prueba de negocio. V1, V3 y V4 empatan con 5/8 porque el repositorio de partida no tenía un comando de arranque documentado, una convención REST declarada ni un manifiesto de dependencias; esas ausencias impedían cumplir los criterios 1, 2 y 8 de forma demostrable. V1 logró una prueba de rechazo incluso con un prompt mínimo, mientras que V3 y V4 lo hicieron con criterios explícitos.

Se seleccionó V4 para integrar a `main` por la calidad de su evidencia, no solo por el puntaje: cubre el estado no final con tareas abiertas, el completado permitido y el completado bloqueado, y mantiene con claridad la regla en el servicio y la adaptación HTTP en la ruta. Después de la escalera se añadieron el comando de arranque, `requirements.txt` y `AGENTS.md`; estas mejoras preparan el proyecto para que el segundo slice requiera un prompt corto sin repetir el contexto.
