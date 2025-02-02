from flask import Flask, request, jsonify
import pandas as pd
import pickle

with open("loan_predictions_kimberly_b.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/invocations", methods=["POST"])
def invocations():
    data = request.get_json()

    df = pd.DataFrame(data['dataframe_split']['data'], columns=data['dataframe_split']['columns'])

    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], errors='coerce')

    predictions = model.predict(df)

    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)