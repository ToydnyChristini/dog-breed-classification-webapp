import streamlit as st
from models.detector import detect
from utils import read_image, bbox_overlay

# construct a dashboard gui
st.title("Dog Breed Classification 🐶 🎖️")
# Add a smaller text as a description within the title using markdown
st.markdown(f"### Developed by Mr. Pavaris Ruangchutiphophan")

# Change the font size using custom CSS
st.markdown(
    """
    <style>
    h3 {
        font-size: 20px;
        color: #333; /* Change the color if needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
upload_img = st.file_uploader(label='Upload Image:', type=["png", "jpg", "jpeg"])

if upload_img:
    img = read_image(upload_img)
    txt_result, prediction, bbox = detect(img)
    # to display text of prediction
    st.text(txt_result)
    # to overlay bounding box onto an image
    bbox_overlay(img, prediction, bbox)


