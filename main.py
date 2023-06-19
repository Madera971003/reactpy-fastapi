
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure, Options
from fastapi import FastAPI

# Components
from components.card.Card import Card

# Styles

app = FastAPI()

@app.get("/saludo")
def principal():
  return {
    "saludo": "Hola Mundo"
  }
  
@app.post("/post_data")
def post_func():
  return {
    "retorno": "Aquí retorno algo"
  }
  
@app.delete("/delete_data")
def delete_func():
  return {
    "retorno": "Se ha eliminado Windows32"
  }
  
@app.patch("/patch_data")
def patch_func():
  return {
    "retorno": "No sé qué hace Patch"
  }
  
@app.put("/put_data")
def put_func():
  return {
    "retorno": "Actualicé datos"
  }

@component
def App():
  return html._(
    html.style(
      "*{margin: 0; padding: 0; box-sizing: border-box; font-family: arial;}",
      """
        .title{
          color: blue;
          padding: 8px;
          text-align: center;
        }
        .cardsContainer {
          padding: 16px;
          display: flex;
          gap: 20px;
          flex-wrap: wrap;
        }
      """
    ),
    html.h1({"class_name": "title"},"Esta es mi nuva App con ReactPy"),
    html.div(
      {"class_name": "cardsContainer"},
      Card("Mi primer Gato", 'https://cdn.onemars.net/sites/nutro_es_NkyIN_B9cV/image/gettyimages-175925832_1615921990619.jpeg'),
      Card("Un segundo Gato", 'https://as01.epimg.net/diarioas/imagenes/2022/04/20/actualidad/1650466413_240889_1650466661_noticia_normal_recorte1.jpg'),
      Card("No está de más un tercer Gato", 'https://beanimalheroes.org/wp-content/uploads/2021/07/tigre-de-bengala-1-800x480-1.jpg'),
      Card("Mi primer Perro", 'https://static.fundacion-affinity.org/cdn/farfuture/PVbbIC-0M9y4fPbbCsdvAD8bcjjtbFc0NSP3lRwlWcE/mtime:1643275542/sites/default/files/los-10-sonidos-principales-del-perro.jpg'),
      Card("Perro Husky", 'https://as01.epimg.net/diarioas/imagenes/2022/05/29/actualidad/1653826510_995351_1653826595_noticia_normal_recorte1.jpg'),
      Card("Un montón de Huskies", 'https://image.ondacero.es/clipping/cmsimages02/2023/02/07/36CCC5BF-2701-40D4-B9A1-DDE104068CC3/que-aullan-perros-hacen-razas-mas-parecidas-lobos_98.jpg?crop=5760,3241,x0,y303&width=1900&height=1069&optimize=high&format=webply'),
      Card("Un conejo", 'https://images.hola.com/imagenes/mascotas/20220825215578/conejos-costumbres-caracteristicas-dn/1-127-664/manias-costumbres-conejos-t.jpg'),
      Card("Un Hamster", 'https://www.mascotanoble.com/wp-content/uploads/2021/02/Tipos-de-Hamsters-Hamster-Dorado.jpg'),
      Card("Ratata", 'https://static.nationalgeographic.es/files/styles/image_3200/public/01-rat-friends-nationalgeographic_1162144.jpg?w=1900&h=1267'),
      Card("Un pokémon", 'https://i.redd.it/h38kbh2bce841.png')
    ),
  )


configure(app, App)