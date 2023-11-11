# COM_UET

Read input from COM, store and plot the data.

## Note:

This program uses Virtual Serial Port Driver to create and connect virtual COM ports, data writing into COM is generated randomly by `WriteIntoCom.py`. Performance on real stuffs has not been tested yet.

## How to use:

Pair two virtual ports COM1 and COM2 using Virtual Serial Port Driver.
Install all libraries in `requirements.txt` using `pip install -r requirements.txt`. If some installations failed, download them manually.
Finally run the `run.py`.

## Thanks
