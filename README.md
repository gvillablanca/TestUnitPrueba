# Testeo de comportamiento con Selenium y python

## Proposito

Para el bimestre en DuocUC se presento el siguiente caso y sobre este mismo se genro pruebas con Selenium automatizadas para la entrega:

### El caso es:

La empresa de desarrollo “System” ha creado un sistema para el inventario de productos el cual ya se encuentra en un avanzado proceso de desarrollo. El equipo, se ha dado cuenta que el sistema no está cumpliendo con algunos requerimientos debido a que no se ha realizado un proceso de pruebas de manera correcta. Es por ello que lo ha contratado a usted, para asesorar a la empresa en la creación de una gestión para el proceso de pruebas, basado en la gestión de inventario.  
1. En la gestión de inventario, el sistema debe ser capaz de:  
- Agregar un nuevo producto 
- Modificar un producto ya ingresado 
- Eliminar un producto existente 
- Buscar un producto 
- Agregar stock de un producto 
- Eliminar stock de un producto 
- Generar un historial de inventario de un producto 
- Los productos deben pertenecer a una categoría de manera obligatoria 
- Los productos deben tener un código y un nombre distinto 
- Los códigos deben tener una longitud obligatoria de 3 dígitos comenzando con la inicial del producto y un número correlativo. 
- Al agregar un nuevo producto el precio solo debe aceptar números enteros.  
 
2. Cualquier persona que pueda trabajar con el sistema debe estar previamente registrado e ingresar con el usuario y contraseña asignado.  
3. Se debe hacer revisión de la ortografía y diseño del sistema. Cualquier problema de esta índole también deberá ser informado como resultado de los casos de prueba. 
4. Comprobar criterios de seguridad del sistema. Para ello debe recomendar mejoras al sistema si encuentra problemas de seguridad como por ejemplo TimeOut de los usuarios. 
5. La base de datos igual debe ser considerada en el proceso de pruebas, indicando problemas de cualquier tipo. (Seguridad, tipos de datos, tiempo de respuesta, etc.) 
6. La empresa cuenta con 20 personas que pueden trabajar de manera simultánea con el sistema, es por ello que se les solicita la ejecución de pruebas que permitan obtener el rendimiento de la aplicación. 


## Correr todos los test con python o shell

Sigue los siquientes pasos para poder ejecutar las pruebas:

1. Clona el repositorio

```
git clone https://github.com/gvillablanca/TestUnitPrueba.git
```

2. Entra al directorio descargado

```
cd  TestUnitPrueba
```

3. Para ejecutar las pruebas con Python haz lo siguiente:

```
python TestingSelenium.py
```

4. Para ejecutar la shell haz lo siguiente:
```
chmod +x TestingSelenium.sh
```
```
./TestingSelenium.sh
```

5. Ejecutado entra a la carpeta de logs
```
cd  Logs
```

Ahi queda el log de lo que se ejecuto y su estado.

6. Ejecutando el Yaml para lanzar las pruebas con un archivo de configuración
```
selenium-side-runner -c config.yaml Simple_Stock.side
```
