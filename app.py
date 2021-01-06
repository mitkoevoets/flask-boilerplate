from flask import Flask, render_template, send_from_directory
from src import controllers

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('views/home.html')


@app.route('/carbon-calculator')
def carbon_calculator():
    return render_template('views/carbon_calculator.html')


app.add_url_rule(
    '/carbon-calculator/run',
    'carbon-calculator-run',
    view_func=controllers.carbon_calculator_controller.run,
    methods=["POST"]
)

if __name__ == '__main__':
    app.run()
