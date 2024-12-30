import genesis as gs
import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg" # replace with the correct ffmpeg path

gs.init(backend=gs.cpu)

scene = gs.Scene(show_viewer=False) # use headless mode

plane = scene.add_entity(
    gs.morphs.Plane(),
)
# franka = scene.add_entity(
#     # gs.morphs.URDF(
#     #     file='urdf/panda_bullet/panda.urdf',
#     #     fixed=True,
#     # ),
#     gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml"),
# )

scene.build()
for i in range(1000):
    scene.step()