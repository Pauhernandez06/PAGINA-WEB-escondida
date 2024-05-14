from flask import Flask
import random

app = Flask(__name__)
facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos", 
              "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
              "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
              "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
              "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
              "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
              "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
              "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]


app = Flask(__name__)
cute_list = ["Sabias que los mosquitos que te pican son hembras?",
            "Sabias que México es el pais numero 2 en violencia?",
            "Sabias que no puedes estornudar con los ojos abiertos?"]

@app.route("/")
def hello_world():
   return f'<h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1><a href="/random_fact">¡Ver un hecho al azar!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/")
def hello_btch():
   return f'<b href="/random_situation">¡Ver una situacion al azar!</b>'

@app.route("/random_situation")
def solution():
    return f'<p2>{random.choice(cute_list)}</p2>'

app.run(debug=True)
