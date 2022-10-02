from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 256
height = 256

# Materiales

brick = Material(diffuse = (2.55, 1.27, 0.8), spec = 16,matType = OPAQUE)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8,matType = OPAQUE)

earth = Material(texture = Texture("earthDay.bmp"))
marble = Material(diffuse = (0.8,0.8,0.8), texture = Texture("marble.bmp"), spec = 32, matType= REFLECTIVE)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior=1.5, matType = TRANSPARENT)
pinkglass = Material(diffuse = (1.55, 0.92, 1.03), spec = 64, ior=1.5, matType = TRANSPARENT)


rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))


# rtx.scene.append(Plane(position=(0,10,0),normal=(0,0,1), material=marble))
rtx.scene.append(Plane(position=(0,-10,-20),normal=(0,1,0), material=earth))
rtx.scene.append(Plane(position=(-50,0,-20),normal=(1,0,0), material=pinkglass))
rtx.scene.append(Plane(position=(50,0,0),normal=(1,0,0), material=brick))
# rtx.scene.append(Plane(position=(0,-10,0),normal=(0,1,0), material=brick))

rtx.scene.append(AABB(position=(2,0,-8),size=(2,2,2), material=stone))
rtx.scene.append(AABB(position=(-1,0,-8),size=(2,2,2), material=brick))


rtx.glRender()

rtx.glFinish("output.bmp")