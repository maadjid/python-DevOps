from flask import Flask, request, render_template, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

# Route principale pour la page d'accueil
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Calculator</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #2c3e50; }
            .container { max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; font-weight: bold; }
            input[type="number"], select { width: 100%; padding: 8px; margin-top: 5px; }
            button { background-color: #3498db; color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 5px; }
            button:hover { background-color: #2980b9; }
            .result { margin-top: 20px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Health Calculator</h1>
            <p>Utilisez les formulaires ci-dessous pour calculer le BMI ou le BMR.</p>
            <h2>Calcul du BMI</h2>
            <form method="post" action="/bmi">
                <div class="form-group">
                    <label for="height">Taille (en mètres) :</label>
                    <input type="number" step="0.01" name="height" required>
                </div>
                <div class="form-group">
                    <label for="weight">Poids (en kilogrammes) :</label>
                    <input type="number" step="0.01" name="weight" required>
                </div>
                <button type="submit">Calculer le BMI</button>
            </form>
            <h2>Calcul du BMR</h2>
            <form method="post" action="/bmr">
                <div class="form-group">
                    <label for="height">Taille (en centimètres) :</label>
                    <input type="number" name="height" required>
                </div>
                <div class="form-group">
                    <label for="weight">Poids (en kilogrammes) :</label>
                    <input type="number" name="weight" required>
                </div>
                <div class="form-group">
                    <label for="age">Âge :</label>
                    <input type="number" name="age" required>
                </div>
                <div class="form-group">
                    <label for="gender">Genre :</label>
                    <select name="gender" required>
                        <option value="male">Homme</option>
                        <option value="female">Femme</option>
                    </select>
                </div>
                <button type="submit">Calculer le BMR</button>
            </form>
        </div>
    </body>
    </html>
    '''

# Route pour calculer le BMI
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'GET':
        return home()
    try:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        result = calculate_bmi(height, weight)
        return f'''
        <div class="container">
            <h1>Résultat du BMI</h1>
            <p>Votre BMI est : <span class="result">{result}</span></p>
            <a href="/">Retour</a>
        </div>
        '''
    except Exception as e:
        return f'<p>Erreur : {str(e)}</p>'

# Route pour calculer le BMR
@app.route('/bmr', methods=['GET', 'POST'])
def bmr():
    if request.method == 'GET':
        return home()
    try:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        result = calculate_bmr(height, weight, age, gender)
        return f'''
        <div class="container">
            <h1>Résultat du BMR</h1>
            <p>Votre BMR est : <span class="result">{result}</span></p>
            <a href="/">Retour</a>
        </div>
        '''
    except Exception as e:
        return f'<p>Erreur : {str(e)}</p>'

# Point d'entrée principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
