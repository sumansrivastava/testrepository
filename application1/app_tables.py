
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/health')
def health():
    return 'OK'
@app.route('/liveness')
def liveness():
    return 'OK'
@app.route('/readiness')
def readiness():
    return 'OK'
@app.route('/tables', methods=['GET', 'POST'])
def tables():
    return render_template('tables_result.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
