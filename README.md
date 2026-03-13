**Proyecto Caso Integrador**
Este proyecto contiene un bot de Telegram para la gestión de inventario de la tienda de Doña Rosa. Los archivos creados cumplen las siguientes funciones:
botRosa.py
Archivo principal en Python que implementa el bot de Telegram. Contiene la conexión a la base de datos SQLite, la creación de la tabla de productos y las funciones para agregar, actualizar, eliminar y consultar productos. Incluye los comandos /add, /update, /delete, /total, /lowstock y /start.
tiendadb
Archivo de base de datos SQLite donde se almacenan los productos. Cada registro guarda nombre, precio, cantidad actual y cantidad inicial. Se utiliza para calcular el costo total del inventario y detectar productos con bajo stock.
.gitignore
Archivo de configuración de Git que indica qué elementos no deben subirse al repositorio. Se usa para excluir el archivo .env que contiene el token del bot y también la base de datos tienda.db si se desea mantenerla privada.
README.md
Documento de referencia que explica la estructura del proyecto, los archivos creados y las funcionalidades implementadas. Sirve como guía para entender el propósito y uso del bot.


**RESPUESTA A PREGUNTA DEL CASO INTEGRADOR**
¿quién garantiza que mis datos (los del negocio) están a salvo?
La seguridad de los datos del negocio depende de cómo se almacenen, en este caso, la base de datos tienda.db está guardada localmente en una base de datos en la computadora, lo que significa que nadie externo tiene acceso, a menos que compartas el archivo o lo subas a un servidor público. La protección se garantiza por la implementación de la persona, se garantiza manteniendo el archivo en un entorno controlado, usando contraseñas seguras en tu sistema, respaldos periódicos y evitando publicar el token del bot o la base de datos en repositorios abiertos de ese modo la confidencialidad del negocio permanecen bajo responsabilidad directa. 
