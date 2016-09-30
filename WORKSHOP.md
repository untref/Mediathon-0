# Workshop

## Descripción del Equipo

Aquí encontrarán una plantilla para completar en la cual podrán especificar los integrantes del equipo que plantea la solución.

[Equipo][4]

Como sugerencia, completenla antes de comenzar con la actividad. Una vez completada les sugerimos que publiquen su solución en el repositorio público.

## Descripción de la actividad

Traducir una dirección habitacional (Ej.: Av. Paseo Colón 850 - C1063ACV - Buenos Aires - Argentina) a una coordenada geo-espacial (latitud, longitud) (-34.617775, -58.368753) generando así un conjunto de datos normalizados y enriquecidos don latitud y longitud.

### Datos de origen
| Evento              | Tipo de dato     | Ejemplo                                   |Comentarios                        |
| ----------------- | --------         | -------                                   |-------                            |
|Identidad          | String           | “507f1f77bcf86cd799439011”                |                                   |
|Dirección          | String           | “Rocha 1264 1ero 4”                       | *Este campo no está normalizado.  |
|Localidad Valor    | String           | “Capital Federa” o “CABA,” o “Cap. Fed.”  | *Este campo no está normalizado.  |
|Provincia Valor    | String           | “Capital Federa” o “CABA”, o “Cap. Fed.”  | *Este campo no está normalizado.  |
|Depende            | String           | “507f1f77bcf86cd799439198”                |                                   |

* Este Campo no está Normalizado: Esto significa que los valores mostrados como ejemplos son algunas de las maneras en las cuales esta información puede ser provista.

### Resultados esperados

| Evento              | Tipo de dato     | Ejemplo                                   |Comentarios                        |
| ----------------- | --------         | -------                                   |-------                            |
|Identidad          | String           | “507f1f77bcf86cd799439011”                |                                   |
|Calle              | String           | “Rocha”                                   | *ver detalle                      |
|Nro Domicilio      | Numero           | 1264                                      | *ver detalle                      |
|Piso               | String           | “A” o “1”                                 | *ver detalle                      |
|Depto              | String           | “4” o “B”                                 | *ver detalle                      |
|Localidad Valor    | String           | “Capital Federa”                          | *ver detalle                      |
|Provincia Valor    | String           | “Capital Federa”                          | *ver detalle                      |
|Latitud            | Numero           |  -34.617775                               | *ver detalle                      |
|Longitud           | Numero           |  -58.368753                               | *ver detalle                      | 


#### Detalle de estructuras

1. Estructura de una dirección
  1. Nombre de la calle: Esta cadena debe corresponderse con algún valor del campo 4 del archivo CSV siguiente (columna 4): 
  2. Número domicilio: Este valor debe corresponderse con algún valor del campo 9 del archivo CSV.
  3. Piso: De no existir se completa el dato con el valor “NINGUNO”.
  4. Depto: De no existir se completa el dato con el valor “NINGUNO”.
2. Estructura de una Localidad: Debe tomar algún valor entre los provistos en la lista de localidades
3. Estructura de una Provincia: Debe tomar algún valor entre los provistos en la lista de provincias
4. Estructura de una Latitud: (https://en.wikipedia.org/wiki/Longitude)
5. Estructura de una Longitud: (https://en.wikipedia.org/wiki/Latitude)

Los datos de latitud y longitud para cada una de las direcciones pueden encontrarse en el archivo de [Frentes y Parcelas][0].

**NOTA:** Dado que el conjunto de direcciones se obtuvieron a partir de los datos publicados<sup>[1](#FuenteDatosParcelas)</sup> por el Gobierno de la ciudad de Buenos Aires estos contendrán sólo información de este distrito. En caso de que algunas de las direcciones provistas pertenezcan a zonas del Gran Buenos Aires estas tendrán como locación la 0.0, 0.0 (latitud, longitud) 

## Descripción de datos

### [Frentes y Parcelas][0]

### [Provincias][1]

### [Localidades][2]

## Publicación de solución 

La publicación de la propuesta prevee que todo el resultado de la colaboración interdisciplinaria quede registrado (públicamente) en el repositorio. Los resultados podrán ser: Assets, Código Fuentes, Modelos Gráficos, Discursos, etc. Es importante al momento de hacer esta publicación (que sugerímos que sea tempranamente aunque incompleta) completar dos archivos en particular: [EQUIPO][4] y [LICENCIA][3].

### Pasos para descargar el workshop y subir la solución

1. Hacer fork del repositorio [https://github.com/untref/Mediathon-0.git](https://github.com/untref/Mediathon-0.git)
2. Clonar repositorio: ```git clone https://github.com/fiuba/Mediathon-0.git```
3. Creación de una rama de trabajo: ```git checkout -b <nombre-equipo>```
4. Completar y/o actualizar los archivos [EQUIPO][4] y [LICENCIA][3].
5. Subir la solución al repo personal ```git push origin <nombre-equipo>/miPropuesta```
6. Confeccionar un PR.

## Licencia 

[MIT][3]

## Notas al pie
1: Datos de parcelas públicos: <a name="#FuenteDatosParcela" href="http://data.buenosaires.gob.ar/">http://data.buenosaires.gob.ar/</a>

[0]: datos/frentesParcelas/DESCRIPCION.md
[1]: datos/provincias/DESCRIPCION.md
[2]: datos/localidades/DESCRIPCION
[3]: LICENCIA.md
[4]: EQUIPO.md

