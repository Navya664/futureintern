from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the calculator
calculator_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .calculator {
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="container calculator">
        <h1 class="text-center">Simple Calculator</h1>
        <form method="POST" action="/">
            <div class="form-group">
                <input type="text" name="num1" class="form-control" placeholder="Enter first number" required>
            </div>
            <div class="form-group">
                <input type="text" name="num2" class="form-control" placeholder="Enter second number" required>
            </div>
            <div class="form-group">
                <select name="operation" class="form-control" required>
                    <option value="">Select Operation</option>
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Calculate</button>
        </form>
        {% if result is not none %}
            <h2 class="mt-4">Result: {{ result }}</h2>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"

    return render_template_string(calculator_html, result=result)

if __name__ == '__main__':
    app.run(debug=True)
pip install Flask
python app.py