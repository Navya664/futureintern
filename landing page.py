from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for the landing page
landing_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container text-center">
        <h1>Welcome to Our Landing Page!</h1>
        <p>This is a simple landing page created with Flask.</p>
        <a href="#" class="btn btn-primary">Get Started</a>
    </div>
</body>
</html>
"""

@app.route('/')
def landing_page():
    return render_template_string(landing_page_html)

if __name__ == '__main__':
    app.run(debug=True)
pip install Flask
python app.py