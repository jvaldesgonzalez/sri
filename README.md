
# Sistema de Recuperación de Información
## Proyecto Final
Yansaro Rodriguez Páez C-512
Javier A. Valdes Gonzalez C-511

### TLDR
Este proyecto se basa en hacer un SRI sobre repositorios de Github haciendo uso de la api de github para repositorios públicos. Entre los features principales encontramos:

1. Operaciones textuales avanzadas
2. Crawling para establecer ranking de repositorios
3. Expansión de consultas
4. Interfaz visual implementada en Flutter


### Procesamiento de Texto
Para el procesamiento de los textos, convertimos la información a texto utf-8. Para ello haremos uso de pdfminer3. Luego de obtener los textos en el formato correcto, hacemos uso de nltk para el procesamiento de estos. 

Primero, este texto es normalizado. Se separan todas las palabras, se llevan a minúscula, se eliminar los caracteres no ASCII y simbolos. Luego se eliminan los stopwords, buscando eliminar las palabras que aportan poca información semántica, como los pronombres, preposiciones y articulos. Luego aplicamos "lemmatizing", buscando eliminar afijos de las palabras, y así computar la forma base de una palabra. 

### Modelo de Recuperación de Información
Como los usuarios no son expertos y el data set es bastante grande, se decidió hacer uso del modelo vectorial.

### Creación de índices
Para la recuperación eficiente de los documentos se necesita crear índices que faciliten los cálculos, el método que se propone es el de Matriz de asociación, donde se guarda la relevancia de los términos en los documentos.
W_(i,j)=relevancia del término t_i  en el documento d_j

### Interfaz de Usuario
Para la interfaz de usuario escogimos como tecnología Flutter, la cual nos permitira compilar para diferentes plataformas y dar un resultado final más placentero y "user friendly".