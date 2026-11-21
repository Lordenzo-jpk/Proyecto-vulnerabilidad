from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name')
    safe_name = escape(name)  # <-- Sanitización
    return f"Hello, {safe_name}!"

if __name__ == '__main__':
    app.run(debug=True)

#Lorenzo Gutierrez