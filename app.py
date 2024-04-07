from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Docker Image Scanner - Powered by Archana Kaushish !!!"


if __name__ == "__main__":
    app.run()
