# Input : .ply
# Output : .ply
# Data Augmentation of Input data
# This script simply creates a random transformation of the input point cloud to generate more data.
# It should be called during the training to generate ad hoc data.

import trimesh
from trimesh import io
mesh = trimesh.load_mesh('plant.ply')
mesh.apply_transform(trimesh.transformations.random_rotation_matrix())
export= io.export.export_obj(mesh)

file = open("export.obj","w")
file.write(export)
file.close()




def get_random_transformation(mesh):
    mesh.apply_transform(trimesh.transformations.random_rotation_matrix())
    return
