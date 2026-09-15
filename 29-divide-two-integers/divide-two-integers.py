class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer boundaries
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle overflow edge case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Bitwise division process
        while dividend >= divisor:
            temp_divisor, count = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1

            dividend -= temp_divisor
            quotient += count

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp result within 32-bit integer limits
        return max(MIN_INT, min(MAX_INT, quotient))