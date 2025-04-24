from flask import Flask, render_template, url_for, request, jsonify
import os

# Configuración de Flask
app = Flask(__name__, static_folder='static', template_folder='templates')

# Página Principal (Landing Page)
@app.route('/')




def home():
    return render_template('home.html', 
                           title="Coders Comerciales", 
                           description="La Comunidad para líderes tech que quieren aprender a venderse mejor y conseguir proyectos.")



# Endpoint Webhook (Para Google Sheets)
@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    print("📩 Datos recibidos:", data)
    return jsonify({"mensaje": "Datos recibidos", "data": data}), 200



if __name__ == '__main__':
    app.run(debug=True)
