# How python works

- When a code is compiled/interpreted it is converted into bytecode which is executed by any python virtual machine

## The main differences between mutable and immutable  

- In python mutable are the values which can be changed in main memory
- In python immutable are the values that we cannot change in main memory
- In order to properly understand the working of python

```python
number1=10
# In python things are bit different like there are no types of variables the only types are of values in main memory like in c++ or other typed language the variables have data type to store values according to the data type but in python this is bit different, python works with references take a look at this example number1=10 the python will create a data type number with value 10 and set reference of number1 variable to the value 10 when change the value of number1 it will look like this number1=20 python will create 20 in main memory and set reference of number1 to 20. The garbage collector of python will delete the values which are not referenced but not immediately because it python thinks may be the variable will refer to the previous values so why spending to much power of these computations 



```
