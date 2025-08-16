import function_list
import unittest

class TestFunctionList(unittest.TestCase):
	def test_that_get_square_exist(self):
		function_list.get_squares(2)
	def test_that_get_square_takes_incorrect_input(self):
		self.assertRaises(TypeError, function_list.get_squares, "Name")
	def test_that_get_squares_returns_correct_value(self):
		result = function_list.get_squares(2)
		self.assertEqual(result , 4)

		result = function_list.get_squares(5)
		self.assertEqual(result , 25)
	def test_that_get_squares_take_zero_as_input(self):
		result = function_list.get_squares(0)
		self.assertEqual(result,0)

	def test_that_get_squares_take_negative_as_input_return_0(self):
		result = function_list.get_squares(-1)
		self.assertEqual(result,0)

class TestFunctionMap(unittest.TestCase):
	def test_that_map_list_take_in_a_list_type(self):
		self.assertRaises(ValueError,function_list.map_list,2)

	def test_that_map_returns_correct_result(self):
		result = function_list.map_list([2,4,5,6,7])
		self.assertEqual(result,[4,16,25,36,49])




class TestFunctionGetlengthOfElement(unittest.TestCase):
	def test_that_get_length_takes_a_collection(self):
		self.assertRaises(ValueError, function_list.get_length,2)
	def test_that_get_length_return_correct_value(self):
		result = function_list.get_length("namr")
		self.assertEqual(result , 4)

		result = function_list.get_length("1")
		self.assertEqual(result , 1)

class TestFunctionListOfLength(unittest.TestCase):
	def test_list_of_length_takes_Incorrectvalue(self):
		self.assertRaises(ValueError,function_list.list_of_length,2)
	def test_list_of_length_returns_correct_value(self):
		result = function_list.list_of_length(["Name","Basit","Ade"])
		self.assertEqual(result,[4,5,3])
		

class TestFunctionfilter(unittest.TestCase):
	def test_that_get_even_takes_incorrect_value(self):
		self.assertRaises(TypeError,function_list.get_even,"name")
	def test_that_get_even_return_corrrect_result(self):
		result = function_list.get_even(2)
		self.assertTrue(result)

	def test_that_get_even_return_corrrect_result(self):
		result = function_list.get_even(3)
		self.assertFalse(result)

class TestFunctionGetEveninlist(unittest.TestCase):
	def test_that_get_even_take_incorrect_result(self):
		self.assertRaises(ValueError,function_list.get_even_list,"Wrog")

	def test_that_get_even_return_correct_value(self):
		result = function_list.get_even_list([2,4,5,7,8,9,11,10])
		self.assertEqual(result, [2,4,8,10])

	def test_that_get_even_list_contain_a_String(self):
		self.assertRaises(TypeError,function_list.get_even_list,["Nmae",2,"Yam"])


		
class TestFunctionItemOfListLengthFive(unittest.TestCase):
	def test_that_function_filter_length_exist(self):
		function_list.filter_length(["Name"])
	def test_that_function_takes_a_values_that_not_a_collection(self):
		self.assertRaises(ValueError,function_list.filter_length, 2)
	def test_that_list_filter_value_contain_values_that_are_not_string(self):
		result = [2,3,4,5]
		self.assertRaises(TypeError,function_list.filter_length,result)
	def test_that_filter_length_return_right_value(self):
		result = function_list.filter_length(["Nmae","Almighty","Badagry","Elemnt"])
		self.assertEqual(result, ["Almighty","Badagry","Elemnt"])
		
	

