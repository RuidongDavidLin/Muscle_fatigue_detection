#!/usr/bin/env python3
import os
import gzip
import shutil
import argparse

def compress_csv_folder(root_dir: str, remove_original: bool = False, compresslevel: int = 9):
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.lower().endswith('.csv'):
                src_path = os.path.join(dirpath, fname)
                dst_path = src_path + '.gz'
                if os.path.exists(dst_path):
                    print(f"[跳过] 已存在：{dst_path}")
                    continue
                with open(src_path, 'rb') as f_in, \
                     gzip.open(dst_path, 'wb', compresslevel=compresslevel) as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print(f"[压缩] {src_path} → {dst_path}")
                if remove_original:
                    os.remove(src_path)
                    print(f"[删除原文件] {src_path}")

def main():
    parser = argparse.ArgumentParser(
        description="一键压缩当前目录及子目录下所有 .csv 文件为 .csv.gz（默认保留原文件）"
    )
    parser.add_argument(
        '--remove-original', '-r',
        action='store_true',
        help="压缩后删除原 .csv 文件"
    )
    parser.add_argument(
        '--level', '-l',
        type=int, default=9, choices=range(1, 10),
        metavar='1-9',
        help="gzip 压缩等级（1 最快 / 压缩率低 … 9 最慢 / 压缩率高，默认9）"
    )
    args = parser.parse_args()
    # 默认根目录为当前工作目录
    compress_csv_folder(os.getcwd(), args.remove_original, args.level)

if __name__ == "__main__":
    main()
