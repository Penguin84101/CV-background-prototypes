import svgwrite
import math
import random

# Tamaño A4 a 300dpi
width, height = 2480, 3508
svg_filename = 'cv_fondo_fullfractales.svg'
png_filename = 'cv_fondo_fullfractales.png'

dwg = svgwrite.Drawing(svg_filename, size=(width, height))
dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='#f9f9f9'))

# Función recursiva de fractal tipo árbol
def branch(x, y, angle, length, depth):
    if depth == 0 or length < 2:
        return
    x2 = x + length * math.cos(angle)
    y2 = y - length * math.sin(angle)
    dwg.add(dwg.line(start=(x, y), end=(x2, y2), stroke='#888888', stroke_width=0.7, opacity=0.15))
    branch(x2, y2, angle + math.pi / 7, length * 0.7, depth - 1)
    branch(x2, y2, angle - math.pi / 7, length * 0.7, depth - 1)

# Distribuir fractales por toda la hoja
n_fractals = 60
for _ in range(n_fractals):
    # Coordenadas aleatorias pero con margen
    x = random.randint(100, width - 100)
    y = random.randint(100, height - 100)
    angle = random.uniform(math.pi / 4, 3 * math.pi / 4)  # crecimiento hacia arriba
    length = random.randint(40, 80)
    depth = random.randint(3, 5)
    branch(x, y, angle, length, depth)

# Guardar SVG
dwg.save()
