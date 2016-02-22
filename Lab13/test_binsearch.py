import unittest
from binsearch import binary_search
import numpy as np

class binaryTest(unittest.TestCase):


	def test_basic(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 5), 5)

	def test_missing(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 4.5), -1)

	#binary search returns the index of one of the repeated elements
	#depending on the length of the array
	def test_repeats(self):
		self.assertEqual(binary_search([2,2,2, 4, 5, 6, 7, 8], 2), 1)		

	def test_repeats2(self):
		self.assertEqual(binary_search([2,2,2, 4, 5], 2), 2)		


	def test_out_or_range(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 10), -1)

	def test_out_of_range2(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, -1), -1)

	def test_emptylist(self):
		input = list()
		self.assertEqual(binary_search(input, 4.5), -1)

	def test_oneelement(self):
		input = list([4])
		self.assertEqual(binary_search(input, 4), 0)

	def test_oneelementmissing(self):
		input = list([4])
		self.assertEqual(binary_search(input, 4.5), -1)

	def test_non_numeric(self):
		input = list(['a','!'])
		with self.assertRaises(TypeError):
			binary_search(input, 4.5)

	def test_infinity(self):
		self.assertEqual(binary_search([1,2,np.inf, np.inf, np.inf], 2), 1)		

	#THIS IS WEIRD. first nan will it touches will return true
	def test_NaN(self):
		self.assertEqual(binary_search([2,np.nan,np.nan, np.nan, np.nan], 2), 2)		

	def test_NaN2(self):
		self.assertEqual(binary_search([2,np.nan, np.nan, 5, np.nan, np.nan, np.nan], 2), 1)		

	def test_needle_basic(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 5, 1, 3), -1)

	def test_needle_basic2(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 5, 3, 7), 5)

	def test_needle_extreme_range(self):
		input = list(range(10))
		with self.assertRaises(IndexError):
			binary_search(input, 5, -1000, 1000)

	def test_needle_singlepoint(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 5, 5, 5), 5)

	def test_needle_singlepoint2(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 5, 6, 6), -1)

	def test_needle_invalidrange(self):
		input = list(range(10))
		self.assertEqual(binary_search(input, 5, 6, 3), -1)

	def test_notalist(self):
		with self.assertRaises(TypeError):
			binary_search(5, 5)

	def test_nparray(self):
		input = np.array(list(range(10)))
		self.assertEqual(binary_search(input, 5), 5)


	def test_notsorted(self):
		self.assertEqual(binary_search([5, 4, 3, 2, 1], 2), -1)		


if __name__ == '__main__':
    unittest.main()