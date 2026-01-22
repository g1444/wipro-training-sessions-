from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "hello this is my first flask server"

if __name__=="__main__":
    app.run(debug=True)