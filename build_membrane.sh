#!/bin/bash
start_time=$(date +%s)
INDIR="/"
OUTDIR="/membrane_param.txt"
cd $INDIR
python membrane_builder.py --x_in=10 --y_in=7 --z_in=2 --x_out=2 --y_out=3 --z_out=1.4 > $OUTDIR&
pid=$!
while kill -0 $pid 2>membrane_builder.err;do
        now=$(date +%s)
        elapsed=$(( now - start_time ))
        echo "Elapsed time: ${elapsed} seconds"
        sleep 1
done
wait $pid
echo -e "\nDone!"
