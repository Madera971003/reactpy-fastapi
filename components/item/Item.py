from reactpy import html, component


@component
def Item(text_value):
  return html._(
      html.style("""
        .itemValue {
          font-size: 12px;
          color: gray;
        }           
      """),
      html.p({"class_name": "itemValue"}, text_value)
    )