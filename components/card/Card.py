from reactpy import html, component, use_state, use_effect

# Components
from components.item.Item import Item

@component
def Card(title, img_url):
  toggle_like, set_toggle_like = use_state(False)
  is_show_description, set_is_show_description = use_state(False)
  
  use_effect(lambda: set_is_show_description(not is_show_description), [toggle_like])
  
  def handle_toggle_like(event):
    set_toggle_like(not toggle_like)
  
  return html.div( {"class_name": "cardContainer"},
    html.style("""
      .cardContainer {
        width: 350px;
        background-color: antiquewhite;
        padding: 14px;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }
      .titleCard {
        text-align: center;
        padding: 10px 0;
      }
      .descriptionCard {
        color: gray;
      }
      .divButton {
        text-align: right;
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .imgContainer {
        width: 100%;
        max-height: 230px;
        margin: 12px 0;
        border-radius: 10px;
      }
      .cardButton {
        padding: 8px;
        color: white;
        width: 80px;
        border: 1px solid gray;
        border-radius: 8px;
      }
      .cardButton:hover {
        cursor: pointer;
      }
    """),
    html.h2({ "class_name": "titleCard"}, title),
    html.p({ "class_name": "descriptionCard"}, "Esto es una pequeña descripción que está un poco larga para ver como se comporta en el navegador."),
    html.div(
      html.img({ "class_name": "imgContainer", "src": img_url, "alt": "Un gato" }),
      Item("Esta descripción depende de asincronismo") if not is_show_description else html._(),
    ),
    html.div(
      { "class_name": "divButton" },
      html.button({ "class_name": "cardButton", "style": {"background_color": "blue" if not toggle_like else "red"}, "on_click": handle_toggle_like }, "Like" if not toggle_like else "Dislike"),
      html.p({"style": { "color": "gray", "font_style": "italic" }}, "You liked this pet") if toggle_like else html._()
    )
  )