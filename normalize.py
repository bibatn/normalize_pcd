import open3d as o3d
import numpy as np


def normalize_pc(points):
    centroid = np.mean(points, axis=0)
    points -= centroid
    furthest_distance = np.max(np.sqrt(np.sum(abs(points)**2,axis=-1)))
    points /= furthest_distance
    return points

def process():
    pcd = o3d.io.read_point_cloud('/home/m/projects_/normalize/samples_for_test/bunny/bunny70k.pcd')
    pcd.remove_non_finite_points()
    xyz = pcd.points
    xyz = np.array(xyz)
    normalize_pc(xyz)
    normalized_pcd = o3d.geometry.PointCloud()
    normalized_pcd.points = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_point_cloud('/home/m/projects_/normalize/samples_for_test/bunny/bunny70k_normalized.pcd', normalized_pcd, write_ascii=True)

if __name__ == '__main__':
    process()