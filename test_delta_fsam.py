import numpy as np
from astropy.io import fits 

import delta_fsam as df

def test_delta_fsam(
    ):
    """ Functionality test for delta_fsam

      It makes use of the transform matrix excam2fsam and fsam2excam to check
      that the application of both transformations is the identity transforatiom.

      See delta_fsam.py for more information about where this data come from.
    """

    # Load delta FSAM to delta EXCAM transformation
    try:
        fsam2excam_matrix = fits.getdata('fsam_to_excam_modelbased.fits')
    except:
        raise FileIOError('The file fsam_to_excam_modelbased.fits is not present.')

    rng = np.random.default_rng(0)
    test_result_list = []
    # Relayive margin on the identity test
    rtol_id = 1e-7
    n_trials = 100
    for idx in range(n_trials):
        # Choose some delta X, delta Y
        delta_xy_pix = np.array([rng.uniform(-100,100), rng.uniform(-100,10)])
        # Appply the transformation to go from delta EXCAM pixels to delta FSAM
        delta_fsam_um = df.delta_fsam(dX_pix=delta_xy_pix[0], dY_pix=delta_xy_pix[1])
        # Apply the inverse operation
        delta_xy_pix_id = fsam2excam_matrix @ delta_fsam_um
        # Assert equality within some margin. Consider
        test_id = np.all(np.abs(delta_xy_pix_id - delta_xy_pix) <= max(np.abs(delta_xy_pix))*rtol_id)
        assert test_id
        test_result_list.append(test_id)

    # Assert all single tests
    assert np.all(test_result_list)
    print('The EXCAM->FSAM test passed')

if __name__ == '__main__':
    test_delta_fsam()
