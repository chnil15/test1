import unittest

class Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_1(self):
		self.assertEqual(3, 3)

if __name__ == '__main__':
	unittest.main()
