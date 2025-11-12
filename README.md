# Colorithm
[**View Live**](https://huggingface.co/spaces/kwiskwis/colorithm)

Colorithm is a Streamlit-powered color palette studio that blends classical computer vision with a deep learning backend to help designers and hobbyists discover cohesive 5-color palettes. Start with an inspiring image or pick a couple of hex values, then let the app extract and refine the remaining shades, preview the result, and download print-ready assets.

---

## Features
- **Dual input modes** – extract hues from any photo using K-Means or seed the model with up to two custom colors.
- **AI refinement** – send the extracted or selected colors to the Colormind deep learning model for harmony-aware suggestions.
- **Interactive previews** – polished color swatches rendered directly inside Streamlit for fast iteration.
- **One-click exports** – download palettes as PNG swatch sheets or JSON payloads for handoff to design tools.
- **Lightweight stack** – simple Python project powered by Streamlit, NumPy, scikit-learn, Pillow, and the Colormind API.
---

## Tech Stack

| Layer        | Tools |
| ------------ | ----- |
| UI / Hosting | Streamlit |
| ML / Data    | scikit-learn, NumPy |
| AI Service   | Colormind API |
| Imaging      | Pillow (PIL) |

---

## Project Structure
```
colorithm/
├── app.py                # Streamlit UI flow
├── requirements.txt      # Python dependencies
└── utils/
    ├── ai_palette.py     # Colormind API helper
    ├── color_utils.py    # Color format conversions
    ├── display_palette.py# Streamlit swatch renderer
    ├── download_utils.py # PNG / JSON export helpers
    └── extract_palette.py# Image-based palette extraction via K-Means
```
---

## Quick Start
1. **Install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run the app**
   ```bash
   streamlit run app.py
   ```
3. Visit the URL printed in your terminal (defaults to `http://localhost:8501`) to start generating palettes, or skip setup entirely and try the hosted demo at [**View Live**](https://huggingface.co/spaces/kwiskwis/colorithm)

---
## Usage Guide
1. **Extract from image**
   - Upload a JPG/PNG; the app downsizes it for speed and runs scikit-learn K-Means to find five dominant colors.
   - Optionally toggle “Refine using AI” to send those colors to Colormind for a harmony-aware remix.
2. **Pick your own colors**
   - Use one or two color pickers to seed the generator when you already know the vibe you’re chasing.
3. **Generate**
   - Click “Generate Final Palette” to blend the inputs with the Colormind model.
   - Review the swatches, then download them as a labeled PNG reference sheet or structured JSON for programmatic use.

---
