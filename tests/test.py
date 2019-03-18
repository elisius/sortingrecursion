from mypackage import myModule

def sum_array(array):
    assert recursion.sum_array([3, 1, 2]) == 6, 'incorrect'
    assert recursion.sum_array([10, 1, 12, 9, 2]) == 34, 'incorrect'
    assert recursion.sum_array([2, 6, 1, 4, 5]) == 18, 'incorrect'

def fibonacci(n):
    assert recursion.fibonacci(3) == 2, 'incorrect'
    assert recursion.fibonacci(2) == 1, 'incorrect'
    assert recursion.fibonacci(1) == 1, 'incorrect'

def factorial(n):
    assert recursion.factorial(1) == 1, 'incorrect'
    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(8) == 40320, 'incorrect'

def reverse(word):
    assert recursion.reverse('hello') == 'olleh', 'incorrect'
    assert recursion.reverse('people') == 'elpoep', 'incorrect'
    assert recursion.reverse('elisius') == 'suisile', 'incorrect'

def bubble_sort(items):
    assert sorting.bubble_sort([54,26,93,17,77,31,44,55,20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93], 'incorrect'
    assert sorting.bubble_sort([3, 1, 2]) == [1,2,3], 'incorrect'
    assert sorting.bubble_sort([5,12,78,1,2,6]) == [1,2,5,6,12,78], 'incorrect'

def merge_sort(items):
    assert sorting.merge_sort([54,26,93,17,77,31,44,55,20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93], 'incorrect'
    assert sorting.merge_sort([3, 1, 2]) == [1,2,3], 'incorrect'
    assert sorting.merge_sort([5,12,78,1,2,6]) == [1,2,5,6,12,78], 'incorrect'

def quick_sort(items):
    assert sorting.quick_sort([54,26,93,17,77,31,44,55,20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93], 'incorrect'
    assert sorting.quick_sort([3, 1, 2]) == [1,2,3], 'incorrect'
    assert sorting.quick_sort([5,12,78,1,2,6]) == [1,2,5,6,12,78], 'incorrect'
