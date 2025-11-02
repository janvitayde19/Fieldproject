import math

float_dividend = 12.5
float_divisor = 5.5

result_percent = float_dividend % float_divisor
result_fmod = math.fmod(float_dividend, float_divisor)

print(f"12.5 % 5.5 = {result_percent}")
print(f"math.fmod(12.5, 5.5) = {result_fmod}")