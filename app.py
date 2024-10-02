from flask import Flask,render_template
from recipe_blueprint import recipe_blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(recipe_blueprint)

@app.route('/')
def home():
    # return "200 OK"
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)