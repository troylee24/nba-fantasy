from flask import Flask, render_template
from parse_data import get_stats

app = Flask(__name__)

@app.route('/')
def index():
    
    stats = get_stats()
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)