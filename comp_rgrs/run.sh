#!/bin/bash
nohup python3 0_boston.py > 0_boston.txt &
nohup python3 0_diabetes.py > 0_diabetes.txt &
nohup python3 0_linnerud.py > 0_linnerud.txt &
nohup python3 0_california.py > 0_california.txt &