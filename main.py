import unittest

class Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_1(self):
		x= 3
		y= 2
		z= x*y
		self.assertEqual(z, 3)
		print(x)
		print(y)
		print(z)

if __name__ == '__main__':
	unittest.main()
