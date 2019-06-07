from bokeh.models import Panel
from bokeh.layouts import row
from bokeh.models.widgets import Div


def gif_tab():
    div = Div(text="""<img src='https://lh3.googleusercontent.com/Nl8wk3VZIT-WIMgok-UwRnpa_UdPBnTi8krVUcH6Ae1a-snbc39gvsgnBKnutWjihQWkDs2HpZR_=s1500' alt='Each Year Map'>""",
              width=1, height=1)

    tab = Panel(child=row(div), title='Each Year Map')

    return tab
