import unittest
import generate_random

class TestGenerateRandom(unittest.TestCase):
	def test_that_get_random_exists(self):	
		generate_random.get_random(1,2)
	def test_that_get_random_generate_a_number_between_1_50(self):
		result = generate_random.get_random(1,51)
		self.assertTrue(result <= 50)

class TestListFunction(unittest.TestCase):
	def test_collet_random_range_and_length_of_list(self):
		generate_random.get_random_range_and_list_size(1,50,10)
	
	def test__range_and_list_size_take_incorrect_start_value(self):
		self.assertRaises(ValueError,generate_random.get_random_range_and_list_size,"Name",2,5)
	
	def test__range_and_list_size_take_incorrect_stop_value(self):
		self.assertRaises(ValueError,generate_random.get_random_range_and_list_size ,5,"Wrong",5)
	
	def test__range_and_list_size_take_incorrect_list_size_value(self):
		self.assertRaises(ValueError,generate_random.get_random_range_and_list_size ,5,9,"Dont")
	
	def test_range_and_list_size_return_a_list_containing_numbers_not_greater_Than_fifty(self):
		result = generate_random.get_random_range_and_list_size(1,50,10)
		for numbers in result:
			self.assertLessEqual(numbers,51)

	
class TestFunctionLength(unittest.TestCase):
	def test_that_get_length_exist(self):
		generate_random.get_length("1")	

	def test_that_get_length_takes_a_values_that_is_not_a_collection(self):
		self.assertRaises(ValueError,generate_random.get_length,1)
	def test_that_get_length_return_correct_values(self):
		result = generate_random.get_length([1,2,3,4,5])
		self.assertEqual(result,5)
		
class TestFunctionEven(unittest.TestCase):
	def test_that_get_even_exist(self):
		generate_random.getEven([2,3])
	def test_that_get_even_take_incorrect_value(self):
		self.assertRaises(TypeError,generate_random.getEven , "Name")

	def test_that_get_even_return_correct_value(self):
		result = (generate_random.getEven([2,9,10,23,17,19]))
		self.assertEqual(result , 27)


class TestFunctionOdd(unittest.TestCase):
	def test_that_get_odd_position_takes_incorrectValue(self):
		self.assertRaises(TypeError,generate_random.get_odd_sum,"Name")
	def test_that_get_odd_returns_correct_result(self):
		result = generate_random.get_odd_sum([15,25,100,25,27,29,28])
		self.assertEqual(result , 79)

class TestFunctionThirdElement(unittest.TestCase):
	def test_that_get_third_position_takes_incorrectValue(self):
		self.assertRaises(TypeError,generate_random.multiply_odd_third,"Name")
	def test_that_get_third_index_returns_correct_result(self):
		result = generate_random.multiply_odd_third([15,25,5,25,27,29,3])
		self.assertEqual(result , 75)

class TestFunctionAverage(unittest.TestCase):
	def test_that_get_average_takes_incorrectValue(self):
		self.assertRaises(TypeError,generate_random.get_average,"Name")
	def test_that_get_average_returns_correct_result(self):
		result = generate_random.get_average([1,4,5,6])
		self.assertEqual(result , 4)

class TestFunctionlargest(unittest.TestCase):
	def test_that_get_largest_takes_incorrectValue(self):
		self.assertRaises(TypeError,generate_random.get_largest,"Name")
	def test_that_get_average_returns_correct_result(self):
		result = generate_random.get_largest([1,4,5,6,15,8,9])
		self.assertEqual(result , 15)

class TestFunctionsmallest(unittest.TestCase):
	def test_that_get_smallest_takes_incorrectValue(self):
		self.assertRaises(TypeError,generate_random.get_smallest,"Name")
	def test_that_get_smallest_returns_correct_result(self):
		result = generate_random.get_smallest([1,4,5,6,15,8,9])
		self.assertEqual(result , 1)






			
	
	