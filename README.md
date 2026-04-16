# ACTIVIDAD M4 L6 - Lectura y Escritura de Archivos en Python

¿Qué diferencia notaste entre write() y append()?

write() abre el archivo en modo 'w', lo que borra todo
el contenido existente y comienza a escribir desde cero.
append() abre el archivo en modo 'a' y agrega el nuevo
contenido al final, sin eliminar lo que ya estaba escrito.

¿Qué ventaja tiene usar with open(...) frente a abrir
y cerrar manualmente?

Con with open(...), Python cierra el archivo de forma
automática al terminar el bloque, aunque ocurra un error.
Al abrir y cerrar manualmente con open() y close(), si
ocurre un error entre ambas instrucciones el archivo
puede quedar abierto, lo que puede causar pérdida de
datos o bloqueo del recurso.