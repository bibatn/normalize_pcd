import numpy as np
import sys


def process(in_file, out_file=''):
    if out_file=='':
        out_file = in_file[:-4] + '_gop.pcd'
    plaintext = np.loadtxt(in_file)
    dist = plaintext[:, 3]
    min_ = np.min(dist, 0)
    max_ = np.max(dist, 0)
    avg = np.sum(dist, 0)/len(dist)
    dist = dist - avg

    sq_diff = np.square(dist)
    av_sq_diff = np.sqrt(np.sum(sq_diff, 0) / (len(sq_diff)-1))
    # av_sq_diff = np.sqrt(np.sum(sq_diff, 0) / len(sq_diff))
    # av_sq_diff = LA.norm(dist)
    print(round(avg, 5), '&', round(av_sq_diff, 5), '&', round(min_, 6), '&', round(max_, 5))



def print_usage():
    print('python3 normalize.py [.pcd filename]')


if __name__ == '__main__':
    if(len(sys.argv)==1):
        print_usage()
    elif(len(sys.argv)==2):
        process(sys.argv[1])
    elif(len(sys.argv)==3):
        process(sys.argv[1], sys.argv[2])