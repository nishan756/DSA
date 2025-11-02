def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    dup_num = abs(x)

    reversed_num = 0
    while dup_num > 0:
        ld = dup_num % 10
        dup_num //= 10
        reversed_num = reversed_num * 10 + ld
    
    if reversed_num >= -2**31 and reversed_num <= 2**31 - 1:
        return sign*reversed_num
    else:
        return 0

print(reverse(120))
print(reverse(-123))
print(reverse(1534236469))