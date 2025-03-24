Automatizar Una Búsqueda

La idea del proyecto es mostrar un buscador automatico de Productos en Mercado libre, la app tiene un interface gráfica con un loguin y dos usuarios, uno lleva a la App de busacr personajes de Rick&Morty (otro de mis proyectos) y el otro user lleva al buscador de Mercado libre.

Se automatizó una búsqueda con Selenium, y nos devuelve en la interface de Tkinter los resultados de los 10 últimos productos encontrados.

Se crea con pip freeze un archivo: "requirements.txt"

Para usar el código solo instalar las librerías con:

	pip install -r requirements.txt

Uso:
Ejecutar directamente el programa con el .exe (no hace falta el código)

Nos dirige a una consola de login donde:

*Si usamos el usuario fede nos lleva a Buscar Personajes:

  Usuario: fede
  
  Contraseña: 2121
  
*Si usamos el usuario mario nos lleva a Buscar Productos:

  Usuario: mario
  
  Contraseña: 2323
  


**BUSCAR PERSONAJES: Poner el nombre de un personaje o cualquier letra en el buscador y presionar "Buscar" para ver la imagen y info extraidas

**BUSCAR PRODUCTOS: Poner el nombre de cualquier cosa que quieras comprar en el buscador y presionar "Buscar"

Tiene un poco de demora (10 a 15s) y nos trae como resultado los 10 últimos productos de la web "https://www.mercadolibre.com.ar/"

  -Nombre
 
  -Precio (pesos Argentinos)
  
  -Compralo ya!! link q nos dirige al producto de la web si le hacemos click

Si borramos y ponemos otro producto y "Buscar" también tiene un poco de demora (20s) pero funciona ok. Estoy trabajando en mejorar los tiempos.
