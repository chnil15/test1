import unittest

class Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_1(self):
		x= 3
		y= 2
		z= x*y
		self.assertEqual(z, 6)

if __name__ == '__main__':
	unittest.main()
