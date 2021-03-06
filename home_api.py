from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>This is a test page from Flask Python</h1>"

@app.route("/testpath")
def hello():
    return "<h1 style='color:blue'>This message is from the test path</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
