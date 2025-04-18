from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for the portfolio website
portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .header {
            background-color: #343a40;
            color: white;
            padding: 20px 0;
        }
        .project {
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            padding: 20px 0;
            background-color: #343a40;
            color: white;
        }
    </style>
</head>
<body>
    <div class="header text-center">
        <h1>My Portfolio</h1>
        <p>Welcome to my personal portfolio website!</p>
    </div>

    <div class="container">
        <h2>About Me</h2>
        <p>Hello! I'm a passionate developer with experience in building web applications. I love coding and creating innovative solutions.</p>

        <h2>Projects</h2>
        <div class="project">
            <h3>Project 1: Awesome App</h3>
            <p>A web application that does amazing things. Built with Flask and React.</p>
        </div>
        <div class="project">
            <h3>Project 2: Portfolio Website</h3>
            <p>This portfolio website showcases my work and skills. Built with Flask.</p>
        </div>
        <div class="project">
            <h3>Project 3: E-commerce Site</h3>
            <p>An online store that allows users to buy products. Built with Django and Bootstrap.</p>
        </div>
    </div>

    <div class="footer">
        <p>Contact me at: <a href="mailto:your-email@example.com" style="color: white;">your-email@example.com</a></p>
        <p>&copy; 2023 My Portfolio</p>
    </div>
</body>
</html>
"""

@app.route('/')
def portfolio():
    return render_template_string(portfolio_html)
if __name__ == '__main__':
    app.run(debug=True)
pip install Flask
python app.py
