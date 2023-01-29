#!/bin/bash
cwd=`pwd`

cd $cwd/cal_data/damBreak
./Allrun
touch run.foam

cd $cwd/cal_data/iobasin
./Allrun
touch run.foam
