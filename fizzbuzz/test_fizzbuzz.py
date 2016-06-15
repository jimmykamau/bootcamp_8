import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
	'''Unittesting FizzBuzz'''

	def test_divisibility_by_three(self):
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'Fizz', msg="should return `Fizz` for number divisible by 3")

	def test_divisibility_by_three(self):
		self.assertEqual(fizzbuzz.fizz_buzz(6), 'Fizz', msg="should return `Fizz` for number divisible by 3")

	def test_divisibility_by_five(self):
		self.assertEqual(fizzbuzz.fizz_buzz(5), 'Buzz', msg="should return `Buzz` for number divisible by 5")

	def test_divisibility_by_five(self):
		self.assertEqual(fizzbuzz.fizz_buzz(10), 'Buzz', msg="should return `Buzz` for number divisible by 5")

	def test_divisibility_by_three_and_five(self):
		self.assertEqual(fizzbuzz.fizz_buzz(15), 'FizzBuzz', msg="should return `FizzBuzz` for number divisible by 3 and 5")

	def test_divisibility_by_three_and_five(self):
		self.assertEqual(fizzbuzz.fizz_buzz(30), 'FizzBuzz', msg="should return `FizzBuzz` for number divisible by 3 and 5")

	def test_divisibility_by_three_and_five(self):
		self.assertEqual(fizzbuzz.fizz_buzz(225), 'FizzBuzz', msg="should return `FizzBuzz` for number divisible by 3 and 5")

	def test_indivisibility(self):
		self.assertEqual(fizzbuzz.fizz_buzz(4), 4, msg="should return the number if it's indivisible by either 3 or 5")

	def test_indivisibility(self):
		self.assertEqual(fizzbuzz.fizz_buzz(28), 28, msg="should return the number if it's indivisible by either 3 or 5")

	# Conflict between returning 'FizzBuzz' and 0
	def test_indivisibility(self):
		self.assertEqual(fizzbuzz.fizz_buzz(0), 'FizzBuzz', msg="should return `FizzBuzz` for number divisible by 3 and 5")