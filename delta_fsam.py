import numpy as np
from astropy.io import fits

def delta_fsam(
    dX_pix=0,
    dY_pix=0,
    ):
    """ Given a selected location on EXCAM, which is dX, dY EXCAM (fractional)
      pixels away from the location of FSAM on EXCAM, return the values of
      dH, dV in micrometers that move FSAM on top of the selected location.

      The values of the EXCAM to FSAM transformation matrix are from the Alfredo
      repository at JPL:

      https://alfresco.jpl.nasa.gov/share/page/site/cgi/documentlibrary?file=readme_transforms.txt#filter=path%7C%2FRoman%20CGI%20Collaboration%20Area%2F04%20-%20Coronagraph%2F15%20-%20CGI%20II%26T%2FInstrument%20Integration%20and%20Test%2FCGI%20I%26T%20Phase%20CD%2FII%26T%20Calibration%20Products%2FTransform%20Matrices

      The file being used in this fucntion is: excam_to_fsam_modelbased.fits

      Reading it with astropy.io.fits.getdata() is:

        array([[  0.   , -10.516],
               [-10.516,   0.   ]], dtype='>f4')

      The file readme_transforms.txt says:
        "excam_to_fsam_modelbased.fits *2x2 matrix. Units of FSAM microns /
         DI+EXCAM pixels. Based purely on designed geometry from optical model.
         Used during TVAC. Chosen as the baseline instead of the FFT-measured
         transform."

      Python algorithm written during TVAC for using FPAM and FSAM matrices

        delta_pam = np.array([[dh], [dv]]) # fill these in
        # read FPAM or FSAM matrices:
        M = np.array([[ M00, M01], [M10, M11]], dtype=float32)
        delta_pix = M @ delta_pam

      Args:
        dX_pix (float): relative X shift with respect to the target pixel for
          acquisition (star). Units are EXCAM pixels.
        dY_pix (float): relative Y shift with respect to the target pixel for
          acquisition (star). Units are EXCAM pixels.
      
      Returns:
        The values of delta H, delta V in micrometers. The output is an array
        whose first value is delta H and the second value is delta V.
    """

    # Read the values of the transform matrix
    try:
        excam2fsam_matrix = fits.getdata('excam_to_fsam_modelbased.fits')
    except:
        raise FileIOError('The file excam_to_fsam_modelbased.fits is not present.')

    # delta X, delta Y on EXCAM in pixel units
    delta_excam_pix = np.array([dX_pix, dY_pix])
    # Expected shifts of FSAM in microns
    delta_fsam_um = excam2fsam_matrix @ delta_excam_pix

    # The output format is delta H, delta V
    return delta_fsam_um
