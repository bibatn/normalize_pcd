import open3d as o3d
import numpy as np
import sys


def normalize_pc(points):
    centroid = np.mean(points, axis=0)
    points -= centroid
    furthest_distance = np.max(np.sqrt(np.sum(abs(points)**2,axis=-1)))
    points /= furthest_distance
    return points


def process(in_file, out_file=''):
    if out_file=='':
        out_file = in_file[:-4] + '_normalized.pcd'
    pcd = o3d.io.read_point_cloud(in_file)
    pcd.remove_non_finite_points()
    xyz = pcd.points
    xyz = np.array(xyz)
    normalize_pc(xyz)
    normalized_pcd = o3d.geometry.PointCloud()
    normalized_pcd.points = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_point_cloud(out_file, normalized_pcd, write_ascii=True)


def print_usage():
    print('python3 normalize.py [.pcd filename]')


if __name__ == '__main__':
    if(len(sys.argv)==1):
        print_usage()
    elif(len(sys.argv)==2):
        process(sys.argv[1])
    elif(len(sys.argv)==3):
        process(sys.argv[1], sys.argv[2])
