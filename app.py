from flask import Flask, render_template, request
import base64
import tensorflow as tf
from keras.utils import img_to_array
import numpy as np
import io
from PIL import Image

app = Flask(__name__)


def predict(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((64, 64))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    punnu_model = tf.keras.models.load_model(r"D:\PROJECT\punnu_detector_v3.h5")

    present = punnu_model.predict(image)
    if present[0][0] == 0:
        # something is there on the skin
        model = tf.keras.models.load_model(r"D:\PROJECT\melanoma_v3.h5")
        ans = model.predict(image)
        val = list(np.argwhere(ans == 1).flatten())
        val = val[1]
        encoded_values = {"melanoma": 0, "nevus": 1, "seborrheic_keratosis": 2}
        for i, k in encoded_values.items():
            if k == val:
                return f"There are chances that you are diagnosed with skin cancer "
    else:

        return "You are all right"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_route():
    image_data = request.form["image"]
    image_bytes = base64.b64decode(image_data)
    result = predict(image_bytes)
    return result


# ... (previous code)


@app.route("/ecommerce")
def e_commerce():
    return render_template("ecom.html")


@app.route("/skindisease")
def skin_disease():
    return render_template("er.html")


@app.route("/doctor")
def dermatologist():
    return render_template("ndoc.html")


@app.route("/community")
def review():
    return render_template("rev.html")


@app.route("/melanoma")
def disease1():
    return render_template("melanoma.html")


@app.route("/keratosis")
def disease2():
    return render_template("keratosis.html")


@app.route("/nevus")
def disease3():
    return render_template("nevus.html")


# ... (previous code)
if __name__ == "__main__":
    app.run(debug=True)
