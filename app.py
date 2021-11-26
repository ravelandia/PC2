import dash
import dash_core_components as dcc
import dash_html_components as html
import mysql.connector

connection=mysql.connector.connect(host='sql',user='sloth',passwd='sloth')
cursor=connection.cursor()

cursor.execute("select MES, BAJO_INFLUENCIA from database.reportes")
enero=cursor.fetchone()
febrero=cursor.fetchone()
marzo=cursor.fetchone()
abril=cursor.fetchone()
mayo=cursor.fetchone()
junio=cursor.fetchone()
julio=cursor.fetchone()
agosto=cursor.fetchone()
septiembre=cursor.fetchone()
octubre=cursor.fetchone()
noviembre=cursor.fetchone()
diciembre=cursor.fetchone()

cursor.execute("select MES, HUBO_MUERTO from database.reportes")
enero1=cursor.fetchone()
febrero1=cursor.fetchone()
marzo1=cursor.fetchone()
abril1=cursor.fetchone()
mayo1=cursor.fetchone()
junio1=cursor.fetchone()
julio1=cursor.fetchone()
agosto1=cursor.fetchone()
septiembre1=cursor.fetchone()
octubre1=cursor.fetchone()
noviembre1=cursor.fetchone()
diciembre1=cursor.fetchone()

cursor.execute("select MES, USO_DE_ARMAS from database.reportes")
enero2=cursor.fetchone()
febrero2=cursor.fetchone()
marzo2=cursor.fetchone()
abril2=cursor.fetchone()
mayo2=cursor.fetchone()
junio2=cursor.fetchone()
julio2=cursor.fetchone()
agosto2=cursor.fetchone()
septiembre2=cursor.fetchone()
octubre2=cursor.fetchone()
noviembre2=cursor.fetchone()
diciembre2=cursor.fetchone()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('main', external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
  html.H1(children='Grupo 2 - PC2'),

  dcc.Graph(
    id='influencia',
    figure={
      'data': [
        {'x': [format(enero[0]), format(febrero[0]), format(marzo[0]), format(abril[0]), format(mayo[0]), format(junio[0]), format(julio[0]), format(agosto[0]), format(septiembre[0]), format(octubre[0]), format(noviembre[0]), format(diciembre[0])], 'y': [format(enero[1]), format(febrero[1]), format(marzo[1]), format(abril[1]), format(mayo[1]), format(junio[1]), format(julio[1]), format(agosto[1]), format(septiembre[1]), format(octubre[1]), format(noviembre[1]), format(diciembre[1])], 'type': 'bar', 'name': 'SF'},
      ],
      'layout': {
        'title': 'Casos con agresores bajo influencia'
      }
    }
  ),
  dcc.Graph(
    id='muertos',
    figure={
      'data': [
        {'x': [format(enero1[0]), format(febrero1[0]), format(marzo1[0]), format(abril1[0]), format(mayo1[0]), format(junio1[0]), format(julio1[0]), format(agosto1[0]), format(septiembre1[0]), format(octubre1[0]), format(noviembre1[0]), format(diciembre1[0])], 'y': [format(enero1[1]), format(febrero1[1]), format(marzo1[1]), format(abril1[1]), format(mayo1[1]), format(junio1[1]), format(julio1[1]), format(agosto1[1]), format(septiembre1[1]), format(octubre1[1]), format(noviembre1[1]), format(diciembre1[1])], 'type': 'bar', 'name': 'SF'},
      ],
      'layout': {
        'title': 'Casos con muertos'
      }
    }
  ),
  dcc.Graph(
    id='armas',
    figure={
      'data': [
        {'x': [format(enero2[0]), format(febrero2[0]), format(marzo2[0]), format(abril2[0]), format(mayo2[0]), format(junio2[0]), format(julio2[0]), format(agosto2[0]), format(septiembre2[0]), format(octubre2[0]), format(noviembre2[0]), format(diciembre2[0])], 'y': [format(enero2[1]), format(febrero2[1]), format(marzo2[1]), format(abril2[1]), format(mayo2[1]), format(junio2[1]), format(julio2[1]), format(agosto2[1]), format(septiembre2[1]), format(octubre2[1]), format(noviembre2[1]), format(diciembre2[1])], 'type': 'bar', 'name': 'SF'},
      ],
      'layout': {
        'title': 'Casos con armas'
      }
    }
  )
])

app.run_server(host='0.0.0.0', port=8080, debug=True)