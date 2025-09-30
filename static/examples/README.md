# Archivos GABC de Ejemplo

Esta carpeta contiene archivos GABC de ejemplo para probar el generador de canto gregoriano.

## Archivos Disponibles

### example.gabc
Un ejemplo básico del Kyrie eleison con notación simple.

### gloria.gabc
Un ejemplo más complejo del Gloria in excelsis Deo con múltiples líneas.

### agnus_dei_viii.gabc
El Agnus Dei VIII completo, uno de los cantos gregorianos más conocidos. Incluye las tres invocaciones tradicionales.

### agnus_dei_simple.gabc
Versión simplificada del Agnus Dei VIII con solo la primera invocación para pruebas rápidas.

### agnus_dei_text.txt
Texto latino completo del Agnus Dei VIII con traducción al español e información musical.

## Formato GABC

GABC es un sistema de notación musical para canto gregoriano que utiliza:

- **Letras del alfabeto** (a-g) para representar las notas
- **Modificadores**:
  - `'` para octava superior (A, B, C, etc.)
  - `,` para octava inferior (a, b, c, etc.)
  - Números para duración (1, 2, 3, 4)
- **Pausas**: `.` (breve), `,` (media), `;` (larga), `:` (muy larga)
- **Agrupaciones**: `()` para agrupar notas

## Estructura del Archivo

```
name:Título del canto;
mode:1;
clef:c;
%%
(c3) Glo(hi)ri(hi)a(gh) in(hi) ex(hi)cel(gh)sis(hi) De(hi)o.(g) (::)
```

- **name**: Título del canto
- **mode**: Modo gregoriano (1-8)
- **clef**: Clave musical (c, f, g)
- **%%**: Separador entre metadatos y música
- **Línea de música**: Notación GABC
- **Línea de letra**: Texto del canto

## Cómo Usar

1. Descarga uno de los archivos de ejemplo
2. Ve a la sección "Gregorio" en el sitio web
3. Arrastra el archivo .gabc al área de carga
4. Configura la voz y velocidad
5. Reproduce el audio generado
6. Sigue la partitura en tiempo real

## Recomendaciones para Pruebas

### Para principiantes:
- **agnus_dei_simple.gabc**: Versión corta y fácil de seguir
- **example.gabc**: Ejemplo básico del Kyrie

### Para usuarios avanzados:
- **agnus_dei_viii.gabc**: Versión completa del Agnus Dei
- **gloria.gabc**: Ejemplo más complejo con múltiples líneas

### Configuración recomendada:
- **Velocidad**: 80-100 BPM para estudio, 120 BPM para audición
- **Voz**: "Coro" para el efecto más auténtico
- **Volumen**: 70-80% para una audición cómoda

## Recursos Adicionales

- [Gregobase](https://gregobase.selapa.net/) - Base de datos de cantos gregorianos
- [Gregorio Documentation](https://gregorio-project.github.io/) - Documentación oficial
- [GABC Tutorial](https://gregorio-project.github.io/gabc/index.html) - Tutorial de notación GABC
