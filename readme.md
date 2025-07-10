# Introduction
This is a assignment for the course "Machine Learning" in CUMTB-2025.

Bofore you want to run my code, please decompress with the specific python script

## Run the script only, compress all .csvs in the current directory and subdirectories, keep the original files

只运行脚本，压缩当前目录及子目录下所有 .csv，保留原文件

python compress_csv.py

## Delete the original .csv after compression

压缩后删除原 .csv

python compress_csv.py --remove-original

## Specify a compression level of 6 (Range From 1 to 9).

指定压缩等级为 6 (Range From 1 to 9)

python compress_csv.py -r -l 6

## Unzip all .csv.gz in the current directory and subdirectories, leaving the archive intact

解压当前目录及子目录下所有 .csv.gz，保留压缩包

python decompress_csv.py

## Unzip and delete .csv.gz

解压后删除 .csv.gz

python decompress_csv.py -r

## The Code Structure

1. Analysis: To deal with the meta data

2. Classifier: To Train and evaluate models