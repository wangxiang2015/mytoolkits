'''
分析时序信号的函数
'''

import numpy as np

def calculate_poincare_statistics(rri, suffix=''):

    def _poincare(rri):
        # Calculate the difference between successive rri's
        diff_rri = np.diff(rri)

        # Calculate SD1 and SD2
        sd1 = np.sqrt(np.std(diff_rri, ddof=1) ** 2 * 0.5)
        sd2 = np.sqrt(2 * np.std(rri, ddof=1) ** 2 - 0.5 * np.std(diff_rri, ddof=1) ** 2)

        return sd1, sd2

    # Empty dictionary
    poincare_statistics = dict()

    # Calculate poincare statistics
    sd1, sd2 = _poincare(rri)

    # Get features
    poincare_statistics['poincare_sd1' + suffix] = sd1
    poincare_statistics['poincare_sd2' + suffix] = sd2

    return poincare_statistics



