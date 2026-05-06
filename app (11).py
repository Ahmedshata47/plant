import streamlit as st
import numpy as np
import json
import os
from PIL import Image
import tensorflow as tf

st.set_page_config(
    page_title="LeafScan — Plant Disease Detector",
    page_icon="🌿",
    layout="centered",
)

@st.cache_resource
def load_model():



    BASE_DIR = os.path.dirname(__file__)

    model_path = os.path.join(BASE_DIR, "plant_model.keras")
    indices_path = os.path.join(BASE_DIR, "class_indices.json")

    

    if not os.path.exists(model_path):
        return None, None, f"Model not found: {model_path}"

    if not os.path.exists(indices_path):
        return None, None, f"class_indices.json not found: {indices_path}"

    model = tf.keras.models.load_model(model_path, compile=False)

    with open(indices_path, "r") as f:
        raw = json.load(f)

    # handle both formats
    if all(str(k).isdigit() for k in raw.keys()):
        class_indices = {int(k): v for k, v in raw.items()}
    else:
        class_indices = {v: k for k, v in raw.items()}

    return model, class_indices, None


def predict(model, class_indices, img):
    img = img.convert("RGB").resize((160, 160))
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)

    preds = model.predict(arr, verbose=0)[0]

    top5_idx = np.argsort(preds)[::-1][:5]
    top5 = [(class_indices.get(i, "Unknown"), float(preds[i]) * 100) for i in top5_idx]

    return top5[0][0], top5[0][1], top5


st.title("🌿 LeafScan - Plant Disease Detector")

model, class_indices, error = load_model()

if error:
    st.error(error)
    st.stop()

st.success(f"Model loaded — {len(class_indices)} classes")

uploaded = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze"):
        with st.spinner("Predicting..."):
            class_name, conf, top5 = predict(model, class_indices, img)

        plant, disease = class_name.split("___") if "___" in class_name else ("Unknown", class_name)

        st.subheader("Result")
        st.write("🌱 Plant:", plant.replace("_", " "))
        st.write("🦠 Disease:", disease.replace("_", " "))
        st.write(f"🎯 Confidence: {conf:.2f}%")

        st.subheader("Top Predictions")
        for name, p in top5:
            st.write(f"{name}: {p:.2f}%")