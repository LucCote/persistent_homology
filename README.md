# persistent_homology

This project is designed to generate barcodes representing the peristent homolgy of pointclouds. To learn more about this topic and how to compute it see other work located [here](https://epjdatascience.springeropen.com/track/pdf/10.1140/epjds/s13688-017-0109-5.pdf)

## vr_persistent_homology.py

Run this script via commandline with ``` python3 vr_persistent_homology.py <file_1> <file_2> ... <file_n>``` where each file is a file containing the text representation of a numpy array representation of a pointcoud
- see the data folder for examples of pointcloud data

This script will generate a plot representing the persisten homology barcodes of the data at homology groups 0, 1, and 2.

## build_vr_complex.py

Run this script via commandline with ``` build_vr_complex.py python3  <file_1> <epsilon 1> <file_2> <epsilon 2>... <file_n> <epsilon n>``` where each file is a file containing the text representation of a numpy array representation of a pointcoud and each epsilon is the epsilon with which you would like to generate the vietoris rips complex of the corresponding file with

This script will generate a plot representing the vietoris rips complex of 2d data at the given epsilon.
