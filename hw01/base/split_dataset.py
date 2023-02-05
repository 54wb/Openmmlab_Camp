import os
import os.path as osp
import sys
from tqdm import tqdm
from shutil import copy,rmtree
import random

def make_dir(dir):
    if osp.exists(dir):
        rmtree(dir)
    os.makedirs(dir)

def split_dataset(src_data_path,target_data_path,val_rate=0.2):
    data_class = [cla for cla in os.listdir(src_data_path)]
    print("CLASSES of this dataset:".format(data_class))
    #create train and test path
    train_data_path = osp.join(target_data_path, "train")
    make_dir(train_data_path)
    for cls in data_class:
        make_dir(osp.join(train_data_path,cls))
    
    val_data_path = osp.join(target_data_path, "val")
    make_dir(val_data_path)
    for cls in data_class:
        make_dir(osp.join(val_data_path, cls))
    
    for cls in tqdm(data_class,desc="spliting"):
        cls_path = osp.join(src_data_path, cls)
        files = os.listdir(cls_path)
        num = len(files)

        val_index = random.sample(files, k = int(num*val_rate))
        for index, file in enumerate(files):
            if file in val_index:
                data_file_path = osp.join(cls_path, file)
                val_target_path = osp.join(val_data_path, cls)
                copy(data_file_path,val_target_path)
            else:
                data_file_path = osp.join(cls_path, file)
                train_target_path = osp.join(train_data_path, cls)
                copy(data_file_path, train_target_path)


def main():
    src_data_path = sys.argv[1]
    target_data_path = sys.argv[2]
    split_dataset(src_data_path, target_data_path)

if __name__ == '__main__':
    main()


