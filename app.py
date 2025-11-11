import streamlit as st

st.set_page_config(page_title="AI Color Palette Generator", page_icon="🎨", layout="centered")

st.title("🎨 AI Color Palette Generator")
st.write("Generate **aesthetic 5-color palettes** using deep learning — inspired by art, films, fashion, and design.")

# Image upload
st.subheader("📸 Option 1: Extract Palette from Image")
uploaded_image = st.file_uploader("Upload a photo or artwork:", type=["jpg", "jpeg", "png"])
use_ai_refine = False
extracted_palette = []

if uploaded_image:
    from PIL import Image
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    # TODO: implement extracted_palette = extract_palette_from_image(img)
    st.subheader("🎨 Extracted Colors")
    # TODO: display_palette(extracted_palette)
    use_ai_refine = st.checkbox("✨ Refine using AI (Colormind)")

# Manual input
st.subheader("🎨 Option 2: Pick Your Own Colors")
col1, col2 = st.columns(2)
base_color1 = col1.color_picker("Base Color 1", "#f0f29a")
use_second = col2.checkbox("Add another base color?")
base_color2 = col2.color_picker("Base Color 2", "#91cdf2") if use_second else None