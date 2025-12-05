def multiply(a, b):
    """
    Multiply two numbers together.
    
    Parameters:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Product of a and b
    """
    return a * b


def main():
    """Demonstrate the multiply function with examples."""
    # Test with integers
    print("Integer multiplication:")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"multiply(10, 12) = {multiply(10, 12)}")
    
    # Test with floats
    print("\nFloat multiplication:")
    print(f"multiply(2.5, 4.0) = {multiply(2.5, 4.0)}")
    print(f"multiply(3.14, 2.0) = {multiply(3.14, 2.0)}")
    
    # Test with negative numbers
    print("\nNegative number multiplication:")
    print(f"multiply(-5, 3) = {multiply(-5, 3)}")
    print(f"multiply(-4, -6) = {multiply(-4, -6)}")
    
    # Test with zero
    print("\nMultiplication with zero:")
    print(f"multiply(100, 0) = {multiply(100, 0)}")
    print(f"multiply(0, 42) = {multiply(0, 42)}")


if __name__ == "__main__":
    main()