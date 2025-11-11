import io
import json
from PIL import Image, ImageDraw

def create_palette_image(hex_colors):
    """Generate a PNG image of the color palette with labels."""
    width = 100 * len(hex_colors)
    height = 120
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    for i, color in enumerate(hex_colors):
        x0 = i * 100
        draw.rectangle([x0, 0, x0 + 100, 100], fill=color)
        draw.text((x0 + 10, 105), color, fill="black", size=10)

    return img

def get_png_bytes(hex_colors):
    """Return palette image as downloadable PNG bytes."""
    img = create_palette_image(hex_colors)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes

def get_json_bytes(hex_colors):
    """Return palette data as downloadable JSON bytes."""
    palette_json = json.dumps({"palette": hex_colors}, indent=2)
    return io.BytesIO(palette_json.encode("utf-8"))
