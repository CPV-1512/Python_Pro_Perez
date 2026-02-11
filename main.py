from flask import Flask, render_template, redirect
import random

app= Flask(__name__)

@app.route("/")
def Inicio():
    return "<h1> Hola desde Python </h1>"

@app.route("/saludo")
def saludo():
    return "<h1> Hola desde mi primera pagina web </h1>"

@app.route("/saludo/<nombre>")
def nombre(nombre):
    return f"<h1> Hola {nombre} bienvenido! </h1>"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"<h1> La suma de {num1} + {num2} es {num1 + num2}</h1> "

@app.route("/datos")
def datos():
    lista_datos =[
        "Según un estudio realizado en 2018, más del 50 por ciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
        "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna"

    ]
    return f"<h1>{random.choice(lista_datos)}</h1>"

@app.route("/moneda")
def tirar_moneda():
   numero= random.randint(1,2)
   if numero == 1:
       return "<h1> Cara </h1>"
   else:
       return "<h1> Sello </h1>"
    
app.run(debug = True)