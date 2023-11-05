import streamlit as st
import os, sys
import pyvista as pv
# import numpy as np
# import plotly.graph_objects as go
# import cadquery as cq

os.system('cls')  # 터미널 창 청소


## Initialize pyvista reader and plotter
reader = pv.STLReader('cylinder.stl')
mesh = reader.read()

plotter = pv.Plotter(border=True, window_size=[580,400]) 
# plotter.background_color = "lightblue"
plotter.add_mesh(mesh, color='white')

## Export to an external pythreejs
model_html = "model.html"
plotter.export_html(model_html)
#plotter.export_html(model_html, backend='pythreejs')

## Read the exported model
with open(model_html,'r') as file: 
    model = file.read()

## Show in webpage
st.components.v1.html(model, height=800)

# # 기본 모델 생성
import cadquery as cq

sphere = cq.Workplane().sphere(5)
base = cq.Workplane(origin=(0, 0, -2)).box(12, 12, 10).cut(sphere).edges("|Z").fillet(2)
sphere_face = base.faces(">>X[2] and (not |Z) and (not |Y)").val()
base = base.faces("<Z").workplane().circle(2).extrude(10)

shaft = cq.Workplane().sphere(4.5).circle(1.5).extrude(20)

spherical_joint = (
    base.union(shaft)
    .faces(">X")
    .workplane(centerOption="CenterOfMass")
    .move(0, 4)
    .slot2D(10, 2, 90)
    .cutBlind(sphere_face)
    .workplane(offset=10)
    .move(0, 2)
    .circle(0.9)
    .extrude("next")
)

result = spherical_joint
# result = cq.Workplane("front").box(2.0, 2.0, 0.5)
# # result = cq.Workplane("front").circle(10).extrude(20)

# # 결과 모델을 STL 파일로 저장
result.val().exportStl("cylinder.stl")

'끝'

print('1')

sys.exit()

import pyvista as pv
import numpy as np

# 기본 도형 생성
cyl = pv.Cylinder()
arrow = pv.Arrow()
sphere = pv.Sphere()
plane = pv.Plane()
line = pv.Line()
box = pv.Box()
cone = pv.Cone()
poly = pv.Polygon()
disc = pv.Disc()

# 사용자 정의 표면 생성
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
grid = pv.StructuredGrid(x, y, z)

# Plotter 생성
p = pv.Plotter(shape=(1, 2))

# 첫 번째 서브플롯에 기본 도형 추가
p.subplot(0, 0)
p.add_mesh(cyl, color="tan", show_edges=True)

# 두 번째 서브플롯에 사용자 정의 표면 추가
p.subplot(0, 1)
p.add_mesh(grid, cmap="coolwarm")

# 플롯 실행
p.show()



'끝'

print('1')

sys.exit()
