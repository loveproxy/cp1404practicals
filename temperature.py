"""Temperature conversion module.

This module provides functions to convert temperatures between Celsius and Fahrenheit.
"""

# No additional imports or constants needed for these calculations.


def main():
    """Main function to demonstrate temperature conversions."""
    # Example temperature values
    celsius_example = 25.0
    fahrenheit_example = 77.0

    # Convert Celsius to Fahrenheit
    converted_fahrenheit = celsius_to_fahrenheit(celsius_example)
    # Convert Fahrenheit to Celsius
    converted_celsius = fahrenheit_to_celsius(fahrenheit_example)

    # Output the results
    print(f"{celsius_example}°C is equivalent to {converted_fahrenheit}°F")
    print(f"{fahrenheit_example}°F is equivalent to {converted_celsius}°C")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    main()
