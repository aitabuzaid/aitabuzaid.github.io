from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/cert')
def cert():
    return render_template("cert.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")



if __name__ == '__main__':
    app.run()
