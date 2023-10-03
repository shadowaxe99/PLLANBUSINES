from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/build', methods=['POST'])
def build_business_plan():
    name = request.form['name']
    investment_amount = request.form['investment-amount']
    # TODO: Implement business plan building logic
    return 'Business plan built'

if __name__ == '__main__':
    app.run(debug=True)