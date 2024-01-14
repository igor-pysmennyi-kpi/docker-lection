from application import app

@app.route('/hello')
def home():
    return "Hello, World!"