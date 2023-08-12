# ProyectoBlog_Simore

## Instrucciones
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:
## Instrucciones para entrar en el panel de admins
+ En la consola ejecutar
```
python manage.py runserver
```
y luego:
```
python manage.py createsuperuser
```
+ crear tu usuario de admin, luego
+ en la dirección agregar /admin/
+ logearte con tu superusuario

+ mi superusuario es admin y contraseña: admin123

## Funcionalidad
+ Tengo mi pagina de inicio, que solamente dice Bienvenidos a mi blog, registrate y sube lo que quieras, la página acerca de mí..
+ Un usuario no logeado puede ver los articulos y su detalle, pero no puede crear ninguno, para ello debe registrarse e iniciar sesión.
+ Ese usuario registrado podrá crear, modificar y eliminar sus propios articulos, pero no podrá con los de otros, además de poder hacer lo mismo que un no registrado

+ Está el formulario artículo y el formulario registro para cada caso
+ Cada usuario puede ver su perfil y editar algún dato si desea

+ Solo un super usuario puede eliminar usuarios
    
