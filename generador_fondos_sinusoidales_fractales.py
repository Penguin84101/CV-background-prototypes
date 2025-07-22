import svgwrite
import math

# Tamaño A4 a 300dpi
width, height = 2480, 3508
svg_filename = 'cv_fondo_fractalfull.svg'

dwg = svgwrite.Drawing(svg_filename, size=(width, height))
dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='#f9f9f9'))

# Parámetros de sinusoides
n_lines = 8
steps = 1000
padding_x = 100
padding_y = 200
opacity_base = 0.15

def branch(x, y, angle, length, depth):
    if depth == 0 or length < 1.5:
        return
    x2 = x + length * math.cos(angle)
    y2 = y - length * math.sin(angle)
    dwg.add(dwg.line(start=(x, y), end=(x2, y2), stroke='#666666', stroke_width=0.5, opacity=0.2))
    branch(x2, y2, angle + math.pi / 7, length * 0.7, depth - 1)
    branch(x2, y2, angle - math.pi / 7, length * 0.7, depth - 1)

for i in range(n_lines):
    freq = 0.005 + i * 0.002
    amp = 100 + i * 20
    phase = i * 0.4
    y_offset = height / 2 + (i - n_lines / 2) * 150

    points = []
    for step in range(steps):
        x = padding_x + step * (width - 2 * padding_x) / steps
        y = y_offset + amp * math.sin(freq * x + phase)
        points.append((x, y))

    # Dibujar la curva principal
    dwg.add(dwg.polyline(points, stroke='#999999', fill='none', stroke_width=1, opacity=opacity_base))

    # Añadir fractales a lo largo de toda la curva
    for idx in range(0, len(points), 60):  # cada 60 puntos aprox
        x, y = points[idx]
        branch(x, y, math.pi / 2, 50, 4)

# Guardar SVG
dwg.save()
