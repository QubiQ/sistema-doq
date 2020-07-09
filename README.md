# sistema-doq
Repositorio para el aprendizaje de Desarollador Odoo QubiQ
Historia de usuario
Yo como usuario quiero [poder registrar libros] para [poder tener una librería en Odoo]

Descripción técnica
Vamos a realizar un nuevo modelo para guardar la siguiente información:

Nombre Libro - Caracteres
Precio -Números con Decimales
Edición - Números Enteros
Fisico o DIgital - Selector
Enlace web de compra - Caracteres
Se ha comprado - Booleano
Fecha de la compra - Fecha y Hora

Posteriormente, añadiremos un punto de menú con un diseño de formulario que separe las posición de los campos por la mitad, además de una lista para ver el nombre, precio y el enlace de los libros que se han registrado.

Consejos

Mirar esta referencia (https://www.odoo.com/documentation/13.0/reference/orm.html#basic-fields) para saber como crear campos Booleanos
Dar permisos al nuevo modelo
Cargar los documentos .py en el __init__.py y .xml en el data del manifest.
