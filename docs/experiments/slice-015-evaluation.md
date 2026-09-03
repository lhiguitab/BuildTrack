# Evaluación del Slice 015: escalera de prompts

La evaluación se hizo sobre el estado de cada rama antes de fusionar V4 a `main`. Los ocho criterios provienen de la guía; la ausencia de alucinaciones se evalúa aparte como noveno criterio. No hay puntuaciones parciales.

| Criterio | V1 | V2 | V3 | V4 |
| --- | --- | --- | --- | --- |
| 1. Arranque con un solo comando documentado | No | No | No | No |
| 2. Ruta según convención REST declarada | No | No | No | No |
| 3. Regla de negocio del RFP | Sí | Sí | Sí | Sí |
| 4. Entrada validada y error estructurado | Sí | Sí | Sí | Sí |
| 5. Estructura y nombres de referencia | Sí | Sí | Sí | Sí |
| 6. Formato de respuesta de referencia | Sí | Sí | Sí | Sí |
| 7. Prueba de la regla de negocio | Sí | No | Sí | Sí |
| 8. Dependencias declaradas | No | No | No | No |
| 9. Sin alucinaciones no solicitadas | Sí | Sí | Sí | Sí |
| **Total** | **6/9** | **5/9** | **6/9** | **6/9** |

## Observaciones

- El repositorio no declaraba una convención REST ni un manifiesto de dependencias; por eso los criterios 2 y 8 no podían cumplirse de forma demostrable en ninguna variante.
- Tampoco existía un comando de arranque documentado en las ramas antes de la fusión; por eso todas fallan el criterio 1.
- V4 empata en el total con V1 y V3, pero se seleccionó porque prueba tres comportamientos: actualización no final con tareas abiertas, completado permitido y completado bloqueado. Además, mantiene de forma explícita la separación entre ruta y servicio.
- Después de la selección se añadieron `requirements.txt` y el comando de arranque al `README.md`; estas mejoras no alteran la puntuación histórica de las ramas.
