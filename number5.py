# Function to convert decimal to binary
def decToBinary(dec):
    if dec == 0:
        return "0"  # Special case for 0
    binary = ""
    while dec > 0:
        # Find the remainder when dividing by 2 (0 or 1)
        remainder = dec % 2
        # Prepend the remainder to the binary string
        binary = str(remainder) + binary
        # Integer division by 2 to update dec
        dec = dec // 2
    return binary


# Function to convert binary to decimal, octal, or hex
def binaryToN(bin_str, type):
    if type == 'decimal':
        decimal = 0
        power = 0
        for digit in bin_str[::-1]:  # Reverse the binary string
            decimal += int(digit) * (2 ** power)
            power += 1
        return decimal
    elif type == 'octal':
        decimal = binaryToN(bin_str, 'decimal')  # Convert binary to decimal
        octal = ""
        while decimal > 0:
            remainder = decimal % 8
            octal = str(remainder) + octal
            decimal = decimal // 8
        return octal
    elif type == 'hex':
        decimal = binaryToN(bin_str, 'decimal')  # Convert binary to decimal
        hex_chars = "0123456789ABCDEF"
        hex_value = ""
        while decimal > 0:
            remainder = decimal % 16
            hex_value = hex_chars[remainder] + hex_value
            decimal = decimal // 16
        return hex_value


# Function to convert decimal to octal
def decToOctal(dec):
    binary = decToBinary(dec)  # Convert decimal to binary
    octal = binaryToN(binary, 'octal')  # Convert binary to octal
    return octal


# Function to convert decimal to hexadecimal
def decToHex(dec):
    binary = decToBinary(dec)  # Convert decimal to binary
    hex_value = binaryToN(binary, 'hex')  # Convert binary to hexadecimal
    return hex_value


# Main function to call all the conversion functions
def main():
    # Input decimal value from the user
    decimal = int(input("Enter a decimal number: "))

    # Convert to binary and display
    binary = decToBinary(decimal)
    print(f"Binary representation: {binary}")

    # Convert binary to decimal and display
    decimal_from_binary = binaryToN(binary, 'decimal')
    print(f"Decimal representation from binary: {decimal_from_binary}")

    # Convert to octal and display
    octal = decToOctal(decimal)
    print(f"Octal representation: {octal}")

    # Convert to hexadecimal and display
    hexadecimal = decToHex(decimal)
    print(f"Hexadecimal representation: {hexadecimal}")


# Call the main function
main()
