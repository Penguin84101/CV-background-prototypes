import svgwrite
import numpy as np
from scipy.spatial import Voronoi
import math
import random

# Dimensiones A4 (300 DPI en pixeles)
width, height = 2480, 3508
svg_file = "cv_fondo_sinusoide_voronoi_fractal.svg"

# Crear documento SVG
dwg = svgwrite.Drawing(svg_file, size=(width, height))
dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='#A9D4DB'))  # Fondo base

# =====================
# 🔷 VORONOI PATTERN
# =====================
num_points = 120
points = np.column_stack((
    np.random.randint(50, width - 50, num_points),
    np.random.randint(50, height - 50, num_points)
))
vor = Voronoi(points)

for region_index in vor.point_region:
    region = vor.regions[region_index]
    if not -1 in region and len(region) > 0:
        polygon = [vor.vertices[i] for i in region]
        dwg.add(dwg.polygon(polygon, fill='none', stroke='#336677', stroke_width=0.7, opacity=0.2))

# =====================
# 🔶 CURVA SINUSOIDAL
# =====================
def sinusoidal_path(freq=0.0025, amp=100, phase=0):
    path_data = []
    for x in range(0, width, 10):
        y = height // 2 + amp * math.sin(freq * x + phase)
        path_data.append((x, y))
    return path_data

sin_path = sinusoidal_path()
for i in range(3):
    offset = i * 150 - 150
    points = [(x, y + offset) for (x, y) in sin_path]
    dwg.add(dwg.polyline(points=points, stroke='#003344', fill='none', stroke_width=1.2, opacity=0.3))

# =====================
# Guardar SVG
# =====================
dwg.save()
print("✅ SVG generado:", svg_file)
