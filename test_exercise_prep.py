# Import the 'unittest' module for writing unit tests. Make no changes to this part.
import unittest
import exercise_prep
from io import StringIO
import sys

p = exercise_prep


# Define a test case class 'PrimeNumberTestCase' that inherits from 'unittest.TestCase'.
# Minimal changes are to be made.
class NumberTestCase(unittest.TestCase):

    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        numbers = []
        for n in range(2, 32): 
            current = p.is_prime(n)
            if current == True:
                numbers.append(n)
        self.assertEqual(numbers, prime_numbers)
    
    def test_backwards(self):
        original_list = ['banana', 'apple', 'melon', 'peach', 'orange', 'apricot']
        backwards_list = ['apricot', 'orange', 'peach', 'melon', 'apple', 'banana']
        answer = p.backwards(original_list)
        self.assertEqual(answer,backwards_list)
    
    def test_factorial_5():
        fac = p.factorial(5)
        self.assertEqual(fac, 120)
    
    def test_factorials_list(self):
        factorials =[]
        for i in range(1,7):
            factorials.append(p.factorial(i))
        self.assertEqual(factorials, [1, 2, 6,24, 120, 720])
    
    def factorial_fail():
        self.assertRaises(TypeError, p.factorial("vibes"))


    def backwards_list_and_prime(self):
        answer_list = [31,29,23,19,17,13,11,7,5,3,2]
        numbers = []
        for n in range(2,32):
            current = p.is_prime(n)
            if current:
                numbers.append(n)
        numbers = p.backwards(numbers)
        self.assertEqual(numbers, answer_list)

    def test_3_triangle(self):
        tri = p.triangle(3)
        self.assertEqual(tri, "1 \n1 2 \n1 2 3")

    def test_7_trianlge(self):
        tri = p.triangle(7)
        self.assertEqual(tri, "1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5 \n1 2 3 4 5 6 \n1 2 3 4 5 6 7")

    def test_pyramid_2(self):

        capture = StringIO()
        sys.stdout = capture
        p.pyramid(2)
        self.assertEqual(capture.getvalue(),""" *
***
""")

    def test_pyramid_6(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        p.pyramid(6)

        self.assertEqual(text_capture.getvalue(),"""     *
    ***
   *****
  *******
 *********
***********
""")
    
    def test_pyramid_19(self):
        capture = StringIO()
        sys.stdout = capture
        p.pyramid(19)
        self.assertEqual(capture.getvalue(), """                  *
                 ***
                *****
               *******
              *********
             ***********
            *************
           ***************
          *****************
         *******************
        *********************
       ***********************
      *************************
     ***************************
    *****************************
   *******************************
  *********************************
 ***********************************
*************************************
""")
    def test_wasnt_me(self):
        files =["shaggy.txt", "shaggy.txt"]
        words =["wasn't me", "red"]
        index = 0
        self.assertEqual(p.word_count(files[index], words[index]), 15)
        self.assertEqual(p.word_count(files[index+1], words[index+1]), 4)

    def test_fibonacci_3(self):
        self.assertEqual(p.fibonacci(3), [0, 1, 1, 2])
    
    def test_fibonacci_9(self):
        self.assertEqual(p.fibonacci(9), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    

if __name__ == '__main__':
    unittest.main()
