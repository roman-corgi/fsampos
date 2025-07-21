This repository contains a function that provides the delta H/V values, in microns, to shift the FSAM from the target point of acquisition to a given 
location on EXCAM, measured in delta EXCAM pixels with respect to the target point of acquisition.

# Dependencies
Numpy, Astropy

# Transformation matrices
The matrices ``fsam_to_excam_modelbased.fits`` and ``excam_to_fsam_modelbased.fits`` contain the four values to translate a delta unity change from 
FSAM to EXCAM and vice versa. See function docstring for more information.

# Unit test
The function ``test_delta_fsam.py`` performs a unit test checking that the transformation returns to its original point when the EXCAM->FSAM->EXCAM transformation is considered. Note: The case ```fsam_to_excam_modelbased.fits`` has extensively been tested in ``corgidrp``. Thus, this function only needs a simpler test.
