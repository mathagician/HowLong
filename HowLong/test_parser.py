import unittest
from HowLong import HowLong


class TestParser(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.parser = HowLong

	def test_empty_arguments(self):
		with self.assertRaises(AssertionError):
			self.parser()

	def test_c_option_with_empty_arguments(self):
		with self.assertRaises(TypeError):
			self.parser('-c')	

	def test_p_option_with_empty_arguments(self):
		with self.assertRaises(TypeError):
			self.parser('-p')


if __name__ == "__main__":
	unittest.main()