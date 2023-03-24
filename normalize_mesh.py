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
        out_file = in_file[:-4] + '_.ply'
    mesh = o3d.io.read_triangle_mesh(in_file)
    # pcd.remove_non_finite_points()
    xyz = mesh.vertices
    xyz = np.array(xyz)
    normalize_pc(xyz)
    mesh.vertices = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_triangle_mesh(out_file, mesh, write_ascii=True)

def print_usage():
    print('python3 normalize.py [.pcd filename]')


if __name__ == '__main__':
    if(len(sys.argv)==1):
        print_usage()
    elif(len(sys.argv)==2):
        process(sys.argv[1])
    elif(len(sys.argv)==3):
        process(sys.argv[1], sys.argv[2])
