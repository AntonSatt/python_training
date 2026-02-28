def calculate_total(price, tax_rate):
    """Calculate total price with tax"""
    # TODO: Fix the type conversion and calculation
    price = "25.00"
    tax_rate = "8"
    
    # This line has a bug
    total = price + (price * tax_rate / 100)
    
    return "Total: $" + total


if __name__ == "__main__":
    result = calculate_total("25.00", "8")
    print(result)
