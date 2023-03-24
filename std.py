# compute average deviation and standard deviation

import open3d as o3d
import numpy as np
import sys


def process(in_file1, in_file2, out_file=''):
    # if out_file=='':
    #     out_file = in_file[:-4] + '_split.pcd'
    pcd1 = o3d.io.read_point_cloud(in_file1)
    pcd2 = o3d.io.read_point_cloud(in_file2)
    # pcd.remove_non_finite_points()
    xyz1 = pcd1.points
    xyz1 = np.array(xyz1)
    xyz2 = pcd2.points
    xyz2 = np.array(xyz2)

    b = np.invert(np.all(xyz2 == [3.4028235e+38, 3.4028235e+38, 3.4028235e+38], 1))
    xyz1 = xyz1[b, :]
    xyz2 = xyz2[b, :]
    diff = xyz1 - xyz2
    diff = np.square(diff)  # L2 norm
    diff = np.sum(diff, 1)  # L2 norm
    diff = np.sqrt(diff)  # L2 norm
    min_ = np.min(diff, 0)
    max_ = np.max(diff, 0)
    av_dev = np.sum(diff, 0)/len(diff)

    sq_diff = np.square(diff)
    av_sq_diff = np.sum(sq_diff, 0)/len(sq_diff)
    print(av_dev, " ", av_sq_diff, " ", max_, " ", min_)



    # splited_pcd = o3d.geometry.PointCloud()
    # splited_pcd.points = o3d.utility.Vector3dVector(xyz)
    # o3d.io.write_point_cloud(out_file, splited_pcd, write_ascii=True)


def print_usage():
    print('python3 std.py [input_1.pcd  input_2.pcd]')


if __name__ == '__main__':
    if(len(sys.argv)==1):
        print_usage()
    elif(len(sys.argv)==3):
        process(sys.argv[1], sys.argv[2])