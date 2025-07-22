import svgwrite
import math
import cairosvg

# Dimensiones A4 a 300dpi
width, height = 2480, 3508
dwg = svgwrite.Drawing('cv_fondo.svg', size=(width, height), profile='full')
dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='#f9f9f9'))

# Parámetros
n_lines = 10
freq_range = (0.005, 0.015)
amplitude_range = (100, 300)
padding = 200
steps = 1000

# Sinusoides
for i in range(n_lines):
    freq = freq_range[0] + i * (freq_range[1] - freq_range[0]) / n_lines
    amp = amplitude_range[0] + i * (amplitude_range[1] - amplitude_range[0]) / n_lines
    phase = i * 0.5
    points = []

    for step in range(steps):
        x = padding + step * (width - 2 * padding) / steps
        y = height / 2 + amp * math.sin(freq * x + phase)
        points.append((x, y))

    # Fractalize the last 10% of the line
    cutoff = int(len(points) * 0.9)
    dwg.add(dwg.polyline(points[:cutoff], stroke='#999999', fill='none', stroke_width=1, opacity=0.15))

    # Fractal part (Pythagorean branch style)
    def branch(x, y, angle, length, depth):
        if depth == 0 or length < 2:
            return
        x2 = x + length * math.cos(angle)
        y2 = y - length * math.sin(angle)
        dwg.add(dwg.line(start=(x, y), end=(x2, y2), stroke='#bbbbbb', stroke_width=0.7, opacity=0.1))
        branch(x2, y2, angle + math.pi / 6, length * 0.7, depth - 1)
        branch(x2, y2, angle - math.pi / 6, length * 0.7, depth - 1)

    # Aplicar ramas en los últimos puntos
    for x, y in points[cutoff::20]:
        branch(x, y, math.pi / 2, 60, 4)

# Guardar SVG
dwg.save()

cairosvg.svg2png(url='cv_fondo.svg', write_to='cv_fondo_fractales.png', dpi=300)

