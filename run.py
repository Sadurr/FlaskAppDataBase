from flask import Flask, render_template, request
from AzureDB import AzureDB

app = Flask(__name__)


@app.route('/')
def hello():
    with AzureDB() as a:
        data = a.azureGetData()
    return render_template("result.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
