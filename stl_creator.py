from scipy.spatial import ConvexHull
from stl import mesh
import numpy as np

def txt_to_stl(points):
    hull = ConvexHull(points)
    
    face_data = np.zeros(len(hull.simplices), dtype=mesh.Mesh.dtype)
    for i, simplex in enumerate(hull.simplices):
        for j in range(3):
            face_data["vectors"][i][j] = points[simplex[j], :]
    
    object_3d = mesh.Mesh(face_data)
    
    return object_3d