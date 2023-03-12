import open3d as o3d
import numpy as np
import sys


def process(in_file, out_file=''):
    if out_file=='':
        out_file = in_file[:-4]
    pcd = o3d.io.read_point_cloud(in_file)
    pcd.remove_non_finite_points()
    xyz = pcd.points
    xyz = np.array(xyz)
    a = []
    b = []
    c = []
    d = []
    count = 0
    for x in xyz:
        if(x[0] > 0 and x[1] > 0):
            a.append(x)
            count += 1
        elif(x[0] > 0 and x[1] < 0):
            b.append(x)
        elif(x[0] < 0 and x[1] > 0):
            c.append(x)
        elif(x[0] < 0 and x[1] < 0):
            d.append(x)
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    
    splited_pcd = o3d.geometry.PointCloud()
    splited_pcd.points = o3d.utility.Vector3dVector(a)
    o3d.io.write_point_cloud(out_file + '_1.pcd', splited_pcd, write_ascii=True)
    
    splited_pcd.points = o3d.utility.Vector3dVector(b)
    o3d.io.write_point_cloud(out_file + '_2.pcd', splited_pcd, write_ascii=True)
    
    splited_pcd.points = o3d.utility.Vector3dVector(c)
    o3d.io.write_point_cloud(out_file + '_3.pcd', splited_pcd, write_ascii=True)
    
    splited_pcd.points = o3d.utility.Vector3dVector(d)
    o3d.io.write_point_cloud(out_file + '_4.pcd', splited_pcd, write_ascii=True)


def print_usage():
    print('python3 split.py [.pcd filename]')


if __name__ == '__main__':
    if(len(sys.argv)==1):
        print_usage()
    elif(len(sys.argv)==2):
        process(sys.argv[1])
    elif(len(sys.argv)==3):
        process(sys.argv[1], sys.argv[2])
