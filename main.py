# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get("button_db")
    correo = request.form.get("email")
    comentario = request.form.get("text")

    with open("comentarios.txt", "a") as f:
        f.write(f"{correo} '\n' ")
        f.write(f"{comentario} '\n' ")
    mensaje = "Tu comentario ha sido enviado"

    return render_template('index.html', button_python=button_python, button_discord=button_discord
                           , button_html=button_html, button_db=button_db, mensaje=mensaje )

    
if __name__ == "__main__":
    app.run(debug=True)
