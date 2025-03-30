

"""
Python Set Operations and Number Types
======================================

This module demonstrates various set operations and different number types in Python,
including their internal implementations and memory representations.

Key concepts covered:
- Set creation, operations, and methods
- Python's number types (int, float, complex, bool, Decimal, Fraction)
- Internal representation of Python data types
- Memory management and optimization techniques

"""

def demonstrate_set_operations() -> None:
    """
    Demonstrates various set operations in Python.
    
    Sets in Python are implemented as hash tables (dictionaries without values).
    They provide O(1) average case complexity for add, remove, and membership testing.
    
    Internally, Python sets:
    - Store only hashable objects (immutable or objects with custom __hash__ methods)
    - Use hash tables with open addressing for collision resolution
    - Maintain at most a 2/3 load factor for performance
    - Are unordered (though as of Python 3.7, insertion order is preserved as an implementation detail)
    
    This function demonstrates:
    1. Creating sets and set conversions
    2. Basic set operations (union, intersection, difference, symmetric difference)
    3. Set methods (add, update, remove, discard, pop, clear)
    4. Set relationships (subset, superset, disjoint)
    5. Frozen sets (immutable variant)
    """
    separator = "=" * 50
    print(separator)
    print("SET OPERATIONS IN PYTHON")
    print(separator)
    
    # Creating sets
    print("\n1. Creating Sets:")
    set1 = {1, 2, 3, 4, 5}  # Set literal syntax, introduced in Python 2.7
    set2 = {4, 5, 6, 7, 8}
    set3 = {1, 2, 3}
    
    # Memory optimization: Python uses shared integer objects for small integers (-5 to 256)
    # This is part of Python's small integer caching mechanism
    
    for i, s in enumerate([set1, set2, set3], 1):
        print(f"set{i} = {s}")
    
    # Creating a set from a list (removes duplicates)
    # Internally, Python iterates through the list and adds each element to the set
    # using the element's hash value to determine its position in the hash table
    list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
    set_from_list = set(list_with_duplicates)
    print(f"\nCreating a set from a list with duplicates {list_with_duplicates}:")
    print(f"set_from_list = {set_from_list}")
    
    # Empty set
    # {} creates an empty dictionary, not a set (historical reason from Python's development)
    empty_set = set()  
    print(f"\nEmpty set: {empty_set}, type: {type(empty_set)}")
    print("Note: {} creates an empty dictionary, not a set")
    
    # Basic Set Operations
    print("\n2. Basic Set Operations:")
    print(f"set1 = {set1}")
    print(f"set2 = {set2}")
    
    # Dictionary to store operations for cleaner display
    # Each operation is shown both with operator syntax and method syntax
    operations = {
        "Union": (set1 | set2, set1.union(set2), "|", "union()"),
        "Intersection": (set1 & set2, set1.intersection(set2), "&", "intersection()"),
        "Difference": (set1 - set2, set1.difference(set2), "-", "difference()"),
        "Symmetric Difference": (set1 ^ set2, set1.symmetric_difference(set2), "^", "symmetric_difference()")
    }
    
    # Internally, these operations create new set objects
    # Python optimizes by short-circuiting when possible (e.g., empty set intersections)
    for op_name, (op_result, method_result, symbol, method_name) in operations.items():
        print(f"{op_name} of set1 and set2 (set1 {symbol} set2): {op_result}")
        print(f"Using {method_name} method: {method_result}")
        # Verify both approaches yield identical results
        print(f"Both results are identical: {op_result == method_result}")
    
    # Set Methods
    print("\n3. Set Methods:")
    
    # Demonstrate set methods with a test set
    test_set = {1, 2, 3}
    print(f"Original set: {test_set}")
    
    # Add element - O(1) average case
    # Internally: Computes hash, finds position, adds element if not present
    test_set.add(4)
    print(f"After add(4): {test_set}")
    
    # Update with multiple elements - O(len(iterable)) time
    # Internally: Iterates through the argument and adds each element
    test_set.update([5, 6, 7])
    print(f"After update([5, 6, 7]): {test_set}")
    
    # Remove element (raises KeyError if element not found)
    # Internally: Computes hash, finds position, removes element if present
    test_set.remove(7)
    print(f"After remove(7): {test_set}")
    
    # Discard element (no error if element not found)
    # Safer alternative to remove() when you're not sure if the element exists
    test_set.discard(10)  # 10 is not in the set, but no error
    print(f"After discard(10): {test_set}")
    
    # Pop an arbitrary element
    # Internally: Removes and returns an arbitrary element
    # The specific element chosen is an implementation detail
    popped = test_set.pop()
    print(f"Popped element: {popped}")
    print(f"After pop(): {test_set}")
    
    # Clear the set
    # Internally: Removes all elements, resets the hash table
    test_set.clear()
    print(f"After clear(): {test_set}")
    
    # Set Relationships
    print("\n3. Set Relationships:")
    print(f"set1 = {set1}")
    print(f"set3 = {set3}")
    
    # Dictionary of relationship tests for cleaner display
    relationships = {
        "Is set3 a subset of set1?": (set3.issubset(set1), set3 <= set1, "issubset()", "<="),
        "Is set1 a superset of set3?": (set1.issuperset(set3), set1 >= set3, "issuperset()", ">="),
        "Is set3 a proper subset of set1?": (set3 < set1, None, "<", None),
        "Is set1 a proper superset of set3?": (set1 > set3, None, ">", None)
    }
    
    # Internally, subset/superset checks iterate through elements
    # with optimizations for empty sets and identical sets
    for question, (operator_result, method_result, operator, method_name) in relationships.items():
        print(f"{question} {operator_result}")
        if method_result is not None:
            print(f"Using {method_name} method: {method_result}")
        print(f"Using {operator} operator: {operator_result}")
    
    # Disjoint sets - sets with no elements in common
    # Internally: Optimized to return early when a common element is found
    print(f"\nAre set1 and set3 disjoint? {set1.isdisjoint(set3)}")
    
    disjoint_set = {10, 11, 12}
    print(f"Are set1 and {disjoint_set} disjoint? {set1.isdisjoint(disjoint_set)}")
    
    # Frozen Sets (immutable sets)
    print("\n5. Frozen Sets:")
    # Internally: Similar to regular sets but doesn't support mutation methods
    # Hash value is computed once and cached for efficiency
    frozen = frozenset([1, 2, 3, 4, 5])
    print(f"Frozen set: {frozen}")
    print(f"Type: {type(frozen)}")
    print("Frozen sets are immutable and can be used as dictionary keys or elements of another set")
    
    # Demonstrate using a frozen set as a dictionary key
    mapping = {frozen: "This is a value mapped to a frozen set key"}
    print(f"Using frozen set as dictionary key: {mapping[frozen]}")
    
    # Set performance characteristics
    print("\n6. Set Performance Characteristics:")
    print("- Average time complexity for add/remove/contains: O(1)")
    print("- Worst case (many hash collisions): O(n)")
    print("- Space complexity: O(n)")
    print("- Sets can only contain hashable (immutable) objects")
    print("- Set elements must be unique")
    print("- As of Python 3.7, insertion order is preserved (implementation detail)")


def demonstrate_number_types():
    """
    Demonstrates different number types in Python.
    
    Python provides several built-in numeric types with different characteristics:
    
    1. Integers (int):
       - Arbitrary precision (no overflow)
       - Implemented as variable-length arrays of digits in base 2³⁰
       - Small integers (-5 to 256) are pre-allocated and shared
    
    2. Floating-point (float):
       - Implemented using C's double (IEEE 754)
       - Typically 53 bits of precision (~15-17 decimal digits)
       - Subject to rounding errors due to binary representation
    
    3. Complex numbers (complex):
       - Pair of floats (real and imaginary parts)
       - Supports standard complex arithmetic
    
    4. Boolean (bool):
       - Subclass of int (True=1, False=0)
       - Optimized for memory usage
    
    5. Decimal:
       - Precise decimal arithmetic
       - Configurable precision
       - Slower than built-in types
    
    6. Fraction:
       - Exact rational number representation
       - Stores numerator and denominator separately
       - Avoids floating-point precision issues
    
    This function demonstrates the properties, operations, and conversions
    between these numeric types.
    """
    print("\n" + "=" * 50)
    print("NUMBER TYPES IN PYTHON")
    print("=" * 50)
    
    # Integers
    print("\n1. Integers (int):")
    print("   Internal implementation: Variable-length array of digits")
    print("   Memory usage: Scales with the magnitude of the number")
    
    regular_int = 42
    big_int = 10**20  # Python handles big integers automatically
    binary_int = 0b1010  # Binary (base 2)
    octal_int = 0o52  # Octal (base 8)
    hex_int = 0x2A  # Hexadecimal (base 16)
    
    print(f"Regular integer: {regular_int}, type: {type(regular_int)}")
    print(f"Big integer: {big_int}, type: {type(big_int)}")
    print(f"Binary (0b1010): {binary_int} (decimal: {binary_int})")
    print(f"Octal (0o52): {octal_int} (decimal: {octal_int})")
    print(f"Hexadecimal (0x2A): {hex_int} (decimal: {hex_int})")
    
    # Integer memory optimization
    print("\n   Integer Memory Optimization:")
    print("   - Small integers (-5 to 256) are pre-allocated and shared")
    print("   - This is why 'a is b' is True when a=b=42, but False when a=b=257")
    
    a, b = 42, 42
    c, d = 257, 257
    print(f"   a=42, b=42: a is b? {a is b}")  # True - same object
    print(f"   c=257, d=257: c is d? {c is d}")  # Likely False - different objects
    
    # Floating-point numbers
    print("\n2. Floating-point numbers (float):")
    print("   Internal implementation: C double (IEEE 754)")
    print("   Precision: ~15-17 decimal digits (53 bits)")
    
    regular_float = 3.14
    scientific_notation = 3.14e10  # 3.14 × 10^10
    
    print(f"Regular float: {regular_float}, type: {type(regular_float)}")
    print(f"Scientific notation: {scientific_notation}")
    
    # Floating-point precision issues
    print("\n   Floating-point Precision Issues:")
    print("   - Binary representation can't exactly represent many decimal fractions")
    print("   - This leads to small rounding errors in calculations")
    print(f"   - Example: 0.1 + 0.2 = {0.1 + 0.2} (not exactly 0.3)")
    print(f"   - Binary representation of 0.1: {float.hex(0.1)}")
    
    # Complex numbers
    print("\n3. Complex numbers (complex):")
    print("   Internal implementation: Pair of floats (real and imaginary parts)")
    
    complex_num = 3 + 4j
    
    print(f"Complex number: {complex_num}, type: {type(complex_num)}")
    print(f"Real part: {complex_num.real}")
    print(f"Imaginary part: {complex_num.imag}")
    print(f"Conjugate: {complex_num.conjugate()}")
    print(f"Absolute value (magnitude): {abs(complex_num)}")
    print(f"Phase (argument) in radians: {__import__('math').atan2(complex_num.imag, complex_num.real)}")
    
    # Boolean (technically a subclass of int)
    print("\n4. Boolean (bool):")
    print("   Internal implementation: Subclass of int (True=1, False=0)")
    print("   Memory optimization: Only two instances exist (True and False)")
    
    print(f"True as int: {int(True)}")
    print(f"False as int: {int(False)}")
    print(f"Is bool a subclass of int? {issubclass(bool, int)}")
    print(f"1 + True = {1 + True}")  # 2
    print(f"True * 5 = {True * 5}")  # 5
    print(f"False * 5 = {False * 5}")  # 0
    
    # Decimal - for precise decimal arithmetic
    print("\n5. Decimal:")
    print("   Internal implementation: Decimal floating point (base 10)")
    print("   Use case: Financial calculations, anywhere exact decimal representation is needed")
    
    from decimal import Decimal, getcontext
    
    getcontext().prec = 28  # Set precision
    
    decimal_num = Decimal('0.1') + Decimal('0.2')
    print(f"Using Decimal for 0.1 + 0.2: {decimal_num}")
    print(f"Type: {type(decimal_num)}")
    print(f"Is exactly 0.3? {decimal_num == Decimal('0.3')}")  # True
    
    # Decimal precision control
    print("\n   Decimal Precision Control:")
    getcontext().prec = 5
    print(f"   With precision=5: {Decimal(1) / Decimal(7)}")
    
    getcontext().prec = 20
    print(f"   With precision=20: {Decimal(1) / Decimal(7)}")
    
    # Fraction - for rational numbers
    print("\n6. Fraction:")
    print("   Internal implementation: Stores numerator and denominator as integers")
    print("   Use case: Exact rational arithmetic, avoiding floating-point errors")
    
    from fractions import Fraction
    
    frac1 = Fraction(1, 3)  # 1/3
    frac2 = Fraction('0.25')  # Converts to 1/4
    
    print(f"Fraction 1/3: {frac1}, type: {type(frac1)}")
    print(f"Fraction from '0.25': {frac2}")
    print(f"Fraction 1/3 + 1/4: {frac1 + Fraction(1, 4)}")
    
    # Converting float to Fraction (showing exact rational representation)
    float_value = 0.1 + 0.2
    fraction_value = Fraction.from_float(float_value)
    print(f"\n   Float 0.1 + 0.2 = {float_value}")
    print(f"   As exact fraction: {fraction_value}")
    print(f"   Simplified: {fraction_value.limit_denominator()}")
    
    # Number type conversions
    print("\n7. Number Type Conversions:")
    print("   Python provides built-in functions for converting between numeric types")
    
    num = 42
    
    print(f"int to float: {float(num)}")
    print(f"int to complex: {complex(num)}")
    print(f"int to bool: {bool(num)} (0 is False, non-zero is True)")
    print(f"int to Decimal: {Decimal(num)}")
    print(f"int to Fraction: {Fraction(num)}")
    
    # Potential conversion issues
    print("\n   Conversion Issues:")
    print("   - float to int truncates (doesn't round)")
    print(f"   - Example: int(3.7) = {int(3.7)}")
    print("   - Some conversions may lose precision")
    print(f"   - Example: Fraction.from_float(0.1) = {Fraction.from_float(0.1)}")
    
    # Math operations and functions
    print("\n8. Math Operations and Functions:")
    print("   Python's math module provides additional mathematical functions")
    
    import math
    
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi: {math.pi}")
    print(f"e: {math.e}")
    print(f"Floor of 3.7: {math.floor(3.7)}")
    print(f"Ceiling of 3.7: {math.ceil(3.7)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
    
    # Numeric type hierarchy and coercion
    print("\n9. Numeric Type Hierarchy and Coercion:")
    print("   When operating on mixed types, Python coerces to the more complex type")
    print("   bool → int → float → complex")
    
    print(f"True + 2 = {True + 2}")  # int (3)
    print(f"3 + 4.5 = {3 + 4.5}")  # float (7.5)
    print(f"3 + 4j + 2 = {3 + 4j + 2}")  # complex (5+4j)
    
    # Numeric limits and special values
    print("\n10. Numeric Limits and Special Values:")
    
    print(f"Infinity: {float('inf')}")
    print(f"Negative Infinity: {float('-inf')}")
    print(f"Not a Number (NaN): {float('nan')}")
    print(f"Is NaN equal to itself? {float('nan') == float('nan')}")  # False
    print(f"Maximum float: {__import__('sys').float_info.max}")
    print(f"Minimum positive float: {__import__('sys').float_info.min}")
    print(f"Float epsilon (smallest representable difference): {__import__('sys').float_info.epsilon}")


if __name__ == "__main__":
    demonstrate_set_operations()
    demonstrate_number_types()
