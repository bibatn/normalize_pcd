import open3d as o3d
import numpy as np
pcd = o3d.io.read_point_cloud('/home/m/projects_/normalize/samples_for_test/bunny/bunny70k.pcd')
pcd.remove_non_finite_points()
xyz = pcd.points
xyz = np.array(xyz)