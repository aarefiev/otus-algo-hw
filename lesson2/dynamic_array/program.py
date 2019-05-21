from model import *
import utils

single_array = SingleArray()
vector_array = VectorArray()
matrix_array = MatrixArray()
factor_array = FactorArray()
# utils.test_add_array(single_array, 10_000)
utils.test_add_array(vector_array, 50_000)
utils.test_add_array(matrix_array, 50_000)
utils.test_add_array(factor_array, 50_000)
