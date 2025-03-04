import unittest
def add(a,b):
    return a+b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(0,1),1)

    # def test_add_with_strings(self):
    #     self.assertRaises(TypeError, add, 'a', 'b')

if __name__ == '__main__':
    unittest.main()