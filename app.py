from flask import Flask, render_template, request
from business_plan_builder import BusinessPlanBuilder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        business_info = request.form
        format = request.form['format']

        # Generate business plan
        builder = BusinessPlanBuilder()
        builder.generate_business_plan(format, business_info)

        return 'Business plan generated!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)