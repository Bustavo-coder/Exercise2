import function_list
import unittest
#mohamed Hesham
class TestFunctionListGetEven(unittest.TestCase):
	def test_that_get_even_return_correct_value(self):
		result = function_list.get_even(2)
		self.assertTrue(result)
	def test_that_get_even_return_correct_value_with_odd_value(self):
		result = function_list.get_even(3)
		self.assertFalse(result)

class TestFunctionFillterCollection(unittest.TestCase):
	def test_that_fillter_collection_take_in_value_that_not_iterable(self):
		self.assertRaises(TypeError,function_list.filter_element,2)
	def test_that_the_element_in_the_iterable_elements_are_not_string(self):
			list_element = ["Name","Cow"]
			self.assertRaises(TypeError,function_list.filter_element,list_element)
	def test_that_filter_element_return_correc_result(self):
		list_element = list(range(1,10))
		result = function_list.filter_element(list_element)
		self.assertEqual(result , [2,4,6,8])

class TestFunctionGetWordOfLengthOfFive(unittest.TestCase):
	def test_that_get_length_take_only_Strings(self):
		self.assertRaises(ValueError,function_list.is_length,2)
	def test_that_is_length_return_correct_result_if_length_is_greater_or_equals_to_five(self):
		result = function_list.is_length("Rahmone")
		self.assertTrue(result)
	def test_that_is_length_return_correct_result_if_length_is_not_five(self):
		result = function_list.is_length("Cow")
		self.assertFalse(result)

class TestFunctionFilterCollectionOfString(unittest.TestCase):
	def test_that_function__filter_string_list_takes_incorrect_value(self):
		self.assertRaises(TypeError , function_list.filters_words,10)
	def test_that_function_filter_string_list_takes_a_list_that_contain_incorrect_values(self):
		element = [1,2,3,4,]
		self.assertRaises(TypeError,function_list.filters_words,element)
	def test_that_function_returns_correct_result(self):
		element = ["Cow","Apple","Balling","Bustavo"]
		result = function_list.filters_words(element)
		self.assertEqual(result,["Apple","Balling","Bustavo",])

class TestFuntionElementIsGreaterThanTwo(unittest.TestCase):
	def test_that_function_is_greater_take_incorrect_input_of_string(self):
		self.assertRaises(ValueError,function_list.is_greater,"str")
	def test_that_function_is_greater_take_incorrect_input_of_negative_int_or_zero(self):
		self.assertRaises(ValueError,function_list.is_greater,-1)
	def test_that_function_is_greater_return_correct_value(self):
		result = function_list.is_greater(4)
		self.assertTrue(result)
	def test_that_function_is_greater_return_correct_value_with_num_less_than_2(self):
		result = function_list.is_greater(1)
		self.assertFalse(result)

class TestFuctionIsDivisibleBy3and5(unittest.TestCase):
	def test_that_function_is_divisible_by_three_n_five_take_incorrect_value(self):
		self.assertRaises(ValueError,function_list.is_divisible_by_three_n_five,"str")
	def test_that_function_is_divisible_by_three_n_five_return_correct_value(self):
		result = function_list.is_divisible_by_three_n_five(15)
		self.assertTrue(result)
	def test_that_function_is_divisible_by_three_n_five_return_correct_value_10(self):
		result = function_list.is_divisible_by_three_n_five(10)
		self.assertFalse(result)

class TestFunctionFilterCollectionDivisibleBy3And5(unittest.TestCase):
	def test_that_filter_collction_num_divided_by_3_n_s_take_invalid_type(self):
		self.assertRaises(TypeError,function_list. filter_collction_num_divided_by_3_n_s,"Nmae")
	def test_that_filter_collection_um_num_divided_by_3_n_s_list_does_not_contain_string(self):
			element = [2,"Nmae","Tyope"]
			self.assertRaises(TypeError,function_list. filter_collction_num_divided_by_3_n_s,element)
	def test_that_filter_collection_um_num_divided_by_3_n_s_returns_correct_value(self):
			element = list(range(1,51))
			result = function_list. filter_collction_num_divided_by_3_n_s(element)
			self.assertEqual(result,[15,30,45])

class TestFunctionIsPalidome(unittest.TestCase):
	def test_that_is_palidome_take_only_Strings(self):
		self.assertRaises(ValueError,function_list.is_palidome,15)
	def test_that_is_palidome_returns_correct_result(self):
		result = function_list.is_palidome("level")
		self.assertTrue(result)
	def test_that_is_palidome_returns_correct_result_2(self):
		result = function_list.is_palidome("Basit")
		self.assertFalse(result)

class TestFunctionFilterPalidonme(unittest.TestCase):
	def test_that_function__filter_collection_palidome_takes_incorrect_value(self):
		self.assertRaises(TypeError , function_list.filter_collection_palidome,15)
	def test_that_function_filter_collection_palidome_takes_a_list_that_contain_incorrect_values(self):
		element = [1,2,3,4,]
		self.assertRaises(TypeError,function_list.filter_collection_palidome,element)
	def test_that_function_filter_collection_palidome_return_correct_result(self):
		element =  ['level','world', 'madam', 'python']
		result = function_list.filter_collection_palidome(element)
		self.assertEqual(result,["level","madam"])
	

	
			
	

		
		
		
	

