# Primer práctico Django

Proyecto realizado con Django.

## Contiene

* App núcleo: `core`
* App temática: `blog`
* Vista principal en `/`
* Vista secundaria en `/posts/`
* Modelo editable desde el panel de administración

## Ejecutar

1. Crear y activar entorno virtual
2. Instalar Django
3. Ejecutar migraciones
4. Correr el servidor

```bash
python -m pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
