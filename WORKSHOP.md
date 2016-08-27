# Workshop

## Descripción de la actividad

Traducir una dirección habitacional (Ej.: Av. Paseo Colón 850 - C1063ACV - Buenos Aires - Argentina) a una coordenada geo-espacial (latitud, longitud) (-34.617775, -58.368753) generando así un conjunto de datos normalizados y enriquecidos don latitud y longitud.

### Datos de origen
| Nodo              | Tipo de dato     | Ejemplo                                   |Comentarios                        |
| ----------------- | --------         | -------                                   |-------                            |
|Identidad          | String           | “507f1f77bcf86cd799439011”                |                                   |
|Dirección          | String           | “Rocha 1264 1ero 4”                       | *Este campo no está normalizado.  |
|Localidad Valor    | String           | “Capital Federa” o “CABA,” o “Cap. Fed.”  | *Este campo no está normalizado.  |
|Provincia Valor    | String           | “Capital Federa” o “CABA”, o “Cap. Fed.”  | *Este campo no está normalizado.  |
|Calle Entre A      | String           | “Hernandarias”                            | *Este campo no está normalizado.  |
|Calle Entre B      | String           | “Av. Regimiento de Patricios”             | *Este campo no está normalizado.  |
|Depende            | String           | “507f1f77bcf86cd799439198”                |                                   |

* Este Campo no está Normalizado: Esto significa que los valores mostrados como ejemplos son algunas de las maneras en las cuales esta información puede ser provista.

### Resultados esperados

| Nodo              | Tipo de dato     | Ejemplo                                   |Comentarios                        |
| ----------------- | --------         | -------                                   |-------                            |
|Identidad          | String           | “507f1f77bcf86cd799439011”                |                                   |
|Calle              | String           | “Rocha”                                   | *ver detalle                      |
|Nro Domicilio      | Numero           | 1264                                      | *ver detalle                      |
|Piso               | String           | “A” o “1”                                 | *ver detalle                      |
|Depto              | String           | “4” o “B”                                 | *ver detalle                      |
|Localidad Valor    | String           | “Capital Federa”                          | *ver detalle                      |
|Provincia Valor    | String           | “Capital Federa”                          | *ver detalle                      |
|Calle Entre A      | String           |  “Hernandarias”                           | *ver detalle                      |
|Calle Entre B      | String           |  “Av. Regimiento de Patricios”            | *ver detalle                      |
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

## Licencia 

[MIT][3]

## Notas al pie
1: <a name="#FuenteDatosParcela" href="http://data.buenosaires.gob.ar/">http://data.buenosaires.gob.ar/</a>

[0]: datos/frentesParcelas/DESCRIPCION.md
[1]: datos/provincias/DESCRIPCION.md
[2]: datos/localidades/DESCRIPCION.
[3]: LICENCIA.md

