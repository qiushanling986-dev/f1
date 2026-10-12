"""Optional Python launcher for the same buildless dashboard."""
from pathlib import Path
from flask import Flask, send_from_directory
ROOT = Path(__file__).parent / 'dist'
app = Flask(__name__, static_folder=str(ROOT), static_url_path='/static')
@app.get('/')
def home():
    return send_from_directory(ROOT, 'index.html')
@app.get('/<path:filename>')
def assets(filename):
    return send_from_directory(ROOT, filename)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
