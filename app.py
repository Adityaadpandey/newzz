from flask import Flask, render_template
# from test import numb
app = Flask(__name__)

# route 1
@app.route("/")
def hello_world():
    return render_template('1.html')



if __name__ == "__main__":
    app.run(debug=True,port=8080)