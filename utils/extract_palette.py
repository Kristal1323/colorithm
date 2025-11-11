import numpy as np
from sklearn.cluster import KMeans
from .color_utils import rgb_to_hex

def extract_palette_from_image(image, n_colors=5):
    img = image.convert("RGB").resize((150, 150))
    data = np.array(img).reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10).fit(data)
    colors = kmeans.cluster_centers_.astype(int)
    return [rgb_to_hex(c) for c in colors]
