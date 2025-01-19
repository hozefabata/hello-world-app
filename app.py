from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return '''
    <form method="post">
        Enter your name: <input type="text" name="name">
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
