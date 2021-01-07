import unittest

def reverseList(arr):
    for i in range(int(len(arr)/2)+1):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    return arr

def isPalindrome(palindrome, reverseWord=""):
    for i in range(len(palindrome)):
        reverseWord+=palindrome[len(palindrome)-1-i]
    return palindrome == reverseWord

def removeNegatives(arr):
    t = len(arr)
    i = 0
    while i < t and t > 0:
        if arr[i] < 0: arr.pop(i)
        t = len(arr)
        i+=1
    if arr[-1] < 0: arr.pop(-1)
    return arr

def coins(val):
    arr = [0,0,0,0]
    while val >= 25:
        arr[0]+=1
        val-=25
    while val >= 10:
        arr[1]+=1
        val-=10
    while val >= 5:
        arr[2]+=1
        val-=5
    arr[3] = val
    return arr

def factorial(n):
    return n*factorial(n-1) if n > 0 else 1

def fib(n):
    return 1 if n<=1 else fib(n-2)+fib(n-1)

class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
    
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3, 4, 2])

class palindromeTest(unittest.TestCase):
    def test1(self):
        return self.assertTrue(isPalindrome("racecar"))
    
    def test2(self):
        return self.assertFalse(isPalindrome('rabcr'))

class removeNegativesTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(removeNegatives([1,3,-5,-7]), [1,3])
    
    def test2(self):
        return self.assertEqual(removeNegatives([-2,1,3,-5,-7]), [1,3])    

class coinTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(87),[3,1,0,2])
    
    def test2(self):
        return self.assertEqual(coins(92),[3,1,1,2])

class factorialTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorial(5), 120)
    
    def test2(self):
        return self.assertEqual(factorial(4), 24)

class fibTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(fib(4), 5)
    
    def test2(self):
        return self.assertEqual(fib(5), 8)

if __name__ == "__main__":
    unittest.main()