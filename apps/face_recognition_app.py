# apps/face_recognition_app.py

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import sys

def run_face_recognition():
    st.title("🛠️ Debug: Face Detection App")

    # 🧠 DEBUG: Print system info
    st.write("### 🔍 Python Info")
    st.write(sys.version)

    st.write("### ✅ Package Versions")
    st.write("cv2 version:", cv2.__version__)
    st.write("numpy version:", np.__version__)

    try:
        st.write("### 🧪 Testing Haar Cascade Load...")
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if face_cascade.empty():
            st.error("❌ Failed to load face cascade.")
            return
        else:
            st.success("✅ Haar cascade loaded successfully.")
    except Exception as e:
        st.error(f"❌ Error loading Haar cascade: {e}")
        return

    # UI: Image input
    img_data = st.camera_input("📸 Capture a photo") or st.file_uploader("Or upload an image", type=["jpg", "jpeg", "png"])

    if img_data:
        try:
            img = Image.open(img_data)
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            st.write(f"Detected {len(faces)} face(s)")

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="Detection Result", use_column_width=True)

        except Exception as e:
            st.error(f"❌ Error processing image: {e}")
