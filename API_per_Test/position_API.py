from flask import Flask, jsonify, request

app = Flask('position_API')

@app.route('/position')
def predict():
    while (True):
        seleccio=input("Rebem peticio, que enviam Null o Posició Ficticia (N/P)")
        if seleccio in ("N","n"):
            return "null"
        if seleccio in ("P","p"):
            result = {
                'X': 20,
                'Y': 10,
                'Angle': 180
            }
            return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
