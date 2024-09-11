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
    button_db = request.form.get('button_db')

    if button_python:
        button_discord = False
        button_html = False
        button_db = False

    elif button_discord:
        button_python = False
        button_html = False
        button_db = False

    elif button_html:
        button_python = False
        button_discord = False
        button_db = False

    elif button_db:
        button_python = False
        button_discord = False
        button_html = False

    return render_template('index.html', button_python=button_python,
                            button_discord=button_discord,
                            button_html=button_html,
                            button_db=button_db)


@app.route('/feedback', methods=['POST'])
def process_feedback():
    email = request.form.get('email')
    text = request.form.get('text')
    with open('form.txt', 'a') as f:
        f.write(f'Email enviado: {email}\n')
        f.write(f'Comentarios enviados: {text}\n')
    return render_template('feedback.html', email=email, text=text)

        
if __name__ == "__main__":
    app.run(debug=True)
