# MLA_Interview

El programa MLA_Interview es un script que se realizó en Python cuya función es buscar en la API de Mercadolibre información sobre items en ventas
de un ID de vendedor especificado por el usuario.

##¿Cómo funciona?
La función "request_data()" arranca pidiendo un usuario de vendedor de la plataforma Mercadolibre.
Se obtiene por medio del request el get de la api del url en cuestión y se llavea con f string el id para que sea genérico
y sirva para generar documentos con ese nombre de ID.
Luego se lo convierte en formato json para poder iterarlo y se van obteniendo y guardando en un log los Value que se obtienen iterando las Keys.
