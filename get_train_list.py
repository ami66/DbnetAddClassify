#!-*- coding=utf-8 -*-

import os
import argparse
def gen_train_file(args):
    label_path = args.label_path
    img_path = args.img_path
    files = os.listdir(img_path)
    with open(os.path.join(args.save_path,'test_list.txt'),'w+',encoding='utf-8') as fid:
        for file in files:
            label_str = os.path.join(img_path,file)+'\t'+os.path.join(label_path,os.path.splitext(file)[0]+'.txt')+'\n'
            fid.write(label_str)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hyperparams')
    parser.add_argument('--label_path', nargs='?', type=str, default='./data/acid/data/test/gt')
    parser.add_argument('--img_path', nargs='?', type=str, default='./data/acid/data/test/img')
    parser.add_argument('--save_path', nargs='?', type=str, default='./data/acid/data/')
    args = parser.parse_args()
    gen_train_file(args)