#!/usr/bin/python3
"""
function multiplication two matrices
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Args
       m_a: matrix
       m_b: matrix
    """
    import numpy as np
    return(np.matmul(m_a, m_b))
