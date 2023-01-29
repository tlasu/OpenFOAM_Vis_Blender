#!/bin/bash

mkdir -p cal_data
cd cal_data

#チュートリアルのデータをもってくる
cp -r $FOAM_TUTORIALS/multiphase/interIsoFoam/damBreak .
cp -r $FOAM_TUTORIALS/multiphase/interIsoFoam/iobasin .
