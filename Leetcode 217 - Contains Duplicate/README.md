# Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# My Approach:
My first approach to solving this problem was using a dictionary. I stored each element in the array as the key with a value of 1. Since dictionaries in Python do not contain duplicate values, a duplicate cannot be stored again. I noticed that if I created a dictionary from the array [1, 2, 3, 1] by setting the keys as the elements in the array and the value( which represents the occurrence) as 1, the dictionary only stored the first 3 elements and not the second 1. i.e {"1": 1, "2": 1, "3": 1}. With this, we can say that if there are duplicates, the length of the dictionary will be less than the length of the array since the duplicate isn't stored in the dictionary. In the example above, the array's length is 4 while the length of the dictionary is 3. However, if there is no duplicate, the length of the dictionary and the length of the array would be the same. 
