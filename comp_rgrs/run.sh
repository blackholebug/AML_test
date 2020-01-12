#!/bin/bash
source activate amlenv
cd Mytest/comp_rgrs

nohup python3 1_eskl.py > 1_eskl.txt 2>&1 &
wait
nohup python3 2_eskl.py > 2_eskl.txt 2>&1 &
wait
nohup python3 3_eskl.py > 3_eskl.txt 2>&1 &
wait
nohup python3 4_eskl.py > 4_eskl.txt 2>&1 &
wait
nohup python3 5_eskl.py > 5_eskl.txt 2>&1 &
wait
nohup python3 10_eskl.py > 10_eskl.txt 2>&1 &
wait
nohup python3 15_eskl.py > 15_eskl.txt 2>&1 &
wait
nohup python3 20_eskl.py > 20_eskl.txt 2>&1 &
wait
nohup python3 25_eskl.py > 25_eskl.txt 2>&1 &
wait
nohup python3 30_eskl.py > 30_eskl.txt 2>&1 &
wait
nohup python3 40_eskl.py > 40_eskl.txt 2>&1 &
wait
nohup python3 50_eskl.py > 50_eskl.txt 2>&1 &
wait
nohup python3 60_eskl.py > 60_eskl.txt 2>&1 &
wait
