from flask import Flask, send_from_directory

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to the Salary Prediction App!"

# Favicon route (you can add a favicon.ico in the 'static' folder)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path + '/static', 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
