#!/usr/bin/env python3
import os
import gzip
import shutil
import argparse

def decompress_gz_folder(root_dir: str, remove_original: bool = False):
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.lower().endswith('.csv.gz'):
                src_path = os.path.join(dirpath, fname)
                dst_path = os.path.join(dirpath, fname[:-3])  # 去掉 '.gz'
                if os.path.exists(dst_path):
                    print(f"[跳过] 目标已存在：{dst_path}")
                    continue
                with gzip.open(src_path, 'rb') as f_in, \
                     open(dst_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print(f"[解压] {src_path} → {dst_path}")
                if remove_original:
                    os.remove(src_path)
                    print(f"[删除压缩包] {src_path}")

def main():
    parser = argparse.ArgumentParser(
        description="一键解压当前目录及子目录下所有 .csv.gz 文件（默认保留压缩包）"
    )
    parser.add_argument(
        '--remove-original', '-r',
        action='store_true',
        help="解压后删除 .csv.gz 文件"
    )
    args = parser.parse_args()
    decompress_gz_folder(os.getcwd(), args.remove_original)

if __name__ == "__main__":
    main()
