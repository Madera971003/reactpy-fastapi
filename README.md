# Aplicación Web hecho con ReactPy y FastAPI

Esta aplicación es hecha con fines prácticos. Se ha probado la nueva herramienta de ReactPy ejecutandose con la librería de uvicorn e instalando FastAPI.

## Instalación de requerimientos

Puedes usar, para evitar conflictos de versiones, un ambiente virtual (comandos para windows).

```bash
py -m venv .venv
```

Es necesario activar el ambiente

```bash
.\.venv\Scripts\activate
```

Por último istalar las librerías

```bash
pip install -r .\requeriments.txt
```

**Nota:** si alguna librería llega a producir conflicto por alguna razón de requirements, debes eliminar esa librería de la lista de requirements.txt y volver a ejecutar el comando.

Las librerías importantes son: FastAPI, ReactPy y uvicorn

## Ejecutar el proyecto

```bash
uvicorn main:app --reload
```

**uvicorn:** es la librería para levantar el proyecto.

**main:** se refiere al archivo main (si cambias el nombre del archivo principal; también cambiar "main").

**app:** este toma la instancia creada de FastAPI (lo puedes encontar dentro de main).

**--reload:** es para que escuche los cambios realizados como desarrollador.