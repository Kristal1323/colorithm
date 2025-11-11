import streamlit as st
from PIL import Image
from utils.ai_palette import generate_ai_palette
from utils.extract_palette import extract_palette_from_image
from utils.color_utils import hex_to_rgb
from utils.display_palette import display_palette 
from utils.download_utils import get_png_bytes, get_json_bytes


st.set_page_config(page_title="Colorithm", page_icon="🎨", layout="centered")

st.title("🎨 Colorithm")
st.write("Generate **aesthetic 5-color palettes** using deep learning — inspired by art, films, fashion, and design.")

# Image upload section
st.subheader("📸 Option 1: Extract Palette from Image")
uploaded_image = st.file_uploader("Upload a photo, artwork, or movie still (optional):", type=["jpg", "jpeg", "png"])

use_ai_refine = False
extracted_palette = []

if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    extracted_palette = extract_palette_from_image(img)
    st.subheader("🎨 Extracted Colors (K-Means)")
    display_palette(extracted_palette)
    use_ai_refine = st.checkbox("✨ Refine using AI for better color harmony")

# Manual input section
st.subheader("🎨 Option 2: Pick Your Own Colors")
col1, col2 = st.columns(2)
base_color1 = col1.color_picker("Base Color 1", "#f0f29a")
use_second = col2.checkbox("Add another base color?")
base_color2 = None
if use_second:
    base_color2 = col2.color_picker("Base Color 2", "#91cdf2")

# Generate final palette
if st.button("🎨 Generate Final Palette"):
    input_colors = []

    if uploaded_image and use_ai_refine:
        input_colors = [hex_to_rgb(c) for c in extracted_palette]
    else:
        if base_color1:
            input_colors.append(hex_to_rgb(base_color1))
        if base_color2:
            input_colors.append(hex_to_rgb(base_color2))

    input_colors = input_colors[:2]

    st.write("Generating palette using deep learning model...")
    palette = generate_ai_palette(input_colors if input_colors else None)

    if palette:
        st.subheader("🎨 Final AI-Generated Palette")
        display_palette(palette)

        # ---------- DOWNLOAD SECTION ----------
        st.markdown("### 💾 Download Your Palette")
        col_img, col_json = st.columns(2)

        with col_img:
            st.download_button(
                label="🖼️ Download as PNG",
                data=get_png_bytes(palette),
                file_name="color_palette.png",
                mime="image/png"
            )

        with col_json:
            st.download_button(
                label="📄 Download as JSON",
                data=get_json_bytes(palette),
                file_name="color_palette.json",
                mime="application/json"
            )

        st.markdown("---")
        st.caption("💡 Save your palette for outfits, interiors, or art inspiration!")


# Footer
st.markdown(
    """
    <div style='text-align:center;margin-top:30px;opacity:0.7;font-size:0.9em'>
        Built by <b>Kristal Sin</b> 
    </div>
    """,
    unsafe_allow_html=True
)
