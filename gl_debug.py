import numpy as np
from glumpy import app, glm, gloo, gl
from glumpy.graphics.collections import SegmentCollection, MarkerCollection
from glumpy.transforms import Position, OrthographicProjection, PanZoom, Viewport
from numpy.random import random

window = app.Window(width=1200, height=600, color=(1,1,1,1))

@window.event
def on_draw(dt):
    window.clear()
    segments.draw()

viewport = Viewport()
transform = PanZoom(OrthographicProjection(Position()))
segments = SegmentCollection(mode="agg", linewidth='local', transform=transform, viewport=viewport)

segments.append([[53, 88, 0]], [[14, 22, 0]],
                linewidth=3, color=(1, 0, 0, 0.1))

for y in np.arange(100, 500, 100):
    segments.append([[0,y,0]], [[100, y, 0]],
                    linewidth = [2], color=[[0, 0, 1, 0.6]])


for x in np.arange(300, 800, 100):
    segments.append([[x,0,0]], [[x, 100, 0]],
                    linewidth = 2, color=[[1, 0, 0, 0.7]])

# segments['antialias'] = 1
window.attach(transform)
window.attach(viewport)
app.run()
