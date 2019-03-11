"""
   Python 正负无穷float('inf')
"""

# 正无穷
float('inf')
# 负无穷
float('-inf')
# 利用 inf 做简单加、乘算术运算仍会得到 inf
print(float('inf') + 100)
print(float('inf') - 100)
print(float('inf') * 100)
print(float('inf') / 100)
print(float('inf') == float('inf') + 100)

# 利用 inf 乘以0会得到 not-a-number(NaN)
print(float('inf') * 0)
print(float('inf') % 100)

# 当涉及 > 和 < 运算时，
# 所有数都比-inf大
# 所有数都比+inf小
print(0 > float('-inf'))
print(10000000 < float('+inf'))

# +inf 和 +inf相等
# -inf 和 -inf相等
print(float('inf') == float('inf'))
print(float('-inf') == float('-inf'))
