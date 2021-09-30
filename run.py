from flask import Flask,render_template
from bibles import create_app

app =  create_app()
#app = Flask(__name__,template_folder="templates")


if __name__=="__main__":
    app.run()