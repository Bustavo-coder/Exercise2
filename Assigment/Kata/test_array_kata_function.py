import unittest
import array_kata

class Testfunction_maximum_int_in_list(unittest.TestCase):
	def test_that_maximum_int_in_list_exist(self):
		array_kata.maximum_int_in_list([10,20,40])

	def test_that_maximum_int_in_list_takes_incorrect_values(self):
		self.assertRaises(TypeError,array_kata.maximum_int_in_list,20)

	def test_that_maximum_int_in_list_returns_the_largest_numbers(self):
		result = array_kata.maximum_int_in_list([10,3,8,15,20])
		self.assertEqual(result,20)
	
		
class Testfunction_minimum_int_in_list(unittest.TestCase):
	def test_that_minimum_int_in_list_exist(self):
		array_kata.minimum_int_in_list([5,3,4])

	def test_that_minimum_int_in_list_takes_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.minimum_int_in_list,"Nmae")
	
	def test_that_minimum_int_in_list_return_the_smallest_int(self):
		result = array_kata.minimum_int_in_list([10,-1,0,-15,-100,10,15])
		self.assertEqual(result,-100)

class Testfunction_sum_of_list(unittest.TestCase):
	def test_that_sum_of_exist(self):
		array_kata.sum_of_list([20,30,40])

	def test_that_sum_of_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.sum_of_list,"Incorrect")

	def test_that_sum_of_list_returns_the_total_sum_of_the_list(self):
		result = array_kata.sum_of_list([15,25,50,100])
		self.assertEqual(result,190)

class Testfunction_sum_of_even_int(unittest.TestCase):
	def test_that_sum_of_even_exists(self):
		array_kata.sum_of_even([20,30,40])
	
	def test_that_sum_of_even_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.sum_of_even,"Incorrect")

	def test_that_sum_of_list_returns_the_total_sum_of_even_in_list(self):
		result = array_kata.sum_of_even([1,2,3,4,5,6,7,8,9,10])
		self.assertEqual(result,30)

class Testfunction_sum_of_odd_int(unittest.TestCase):
	def test_that_sum_of_odd_exists(self):
		array_kata.sum_of_odd([15,12,10])
	
	def test_that_sum_of_odd_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.sum_of_odd,"Incorrect")

	def test_that_sum_of_list_returns_the_total_sum_of_odd_in_list(self):
		result = array_kata.sum_of_odd([1,2,3,4,5,6,7,8,9,10])
		self.assertEqual(result,25)



class Testfunction_maximum_minimum_int_in_list(unittest.TestCase):
	def test_that_maximum_minimum_exists(self):
		array_kata.maximum_minimum_int_in_list([15,12,10])
	
	def test_that_maximum_minimum_int_in_list_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.maximum_minimum_int_in_list,"Incorrect")

	
	def test_that_maximum_minimum_int_in_list_return_a_list_containig_minmum_maximum(self):
		result = array_kata.maximum_minimum_int_in_list([1,2,3,4,5,6,7,8,9,10])
		self.assertEqual(result,[1,10])


class Testfunction_numbers_of_odd_int(unittest.TestCase):
	def test_that_numbers_of_odd_exists(self):
		array_kata.numbers_of_odd([15,12,10,18,70])
	
	def test_that__numbers_of_odd_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.numbers_of_odd,"Incorrect")

	def test_that_sum_of_list_returns_the_total_numbers_of_odd_in_list(self):
		result = array_kata.numbers_of_odd([1,2,3,4,5,6,7,8,9,10])
		self.assertEqual(result,5)



class Testfunction_numbers_of_even_int(unittest.TestCase):
	def test_that_numbers_of_even_exists(self):
		array_kata.numbers_of_even([15,12,10])
	
	def test_that__numbers_of_even_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.numbers_of_even,"Incorrect")

	def test_that_sum_of_list_returns_the_total_numbers_of_even_in_list(self):
		result = array_kata.numbers_of_even([1,2,3,4,5,6,7,8,9,10])
		self.assertEqual(result,5)

class Testfunction_even_numbers_in_list(unittest.TestCase):
	def test_that_even_numbers_in_list_exists(self):
		array_kata.even_numbers_in([15,12,10])
	
	def test_that_even_numbers_in_list_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.even_numbers_in,"Incorrect")

	def test_that_even_numbers_in_list_return_a_list_containig_even_numbers(self):
		result = array_kata.even_numbers_in([2,3,5,7,9,10,15,19,20])
		self.assertEqual(result,[2,10,20])



class Testfunction_odd_numbers_in_list(unittest.TestCase):
	def test_that_odd_numbers_in_list_exists(self):
		array_kata.odd_numbers_in([15,12,10])
	
	def test_that_odd_numbers_in_list_take_incorrect_value(self):
		self.assertRaises(TypeError,array_kata.odd_numbers_in,"Incorrect")

	def test_that_odd_numbers_in_list_return_a_list_containig_odd_numbers(self):
		result = array_kata.odd_numbers_in([2,3,5,7,9,10,15,19,20])
		self.assertEqual(result,[3, 5, 7, 9, 15, 19])


