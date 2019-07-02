# code-golf:

n = int(input())
print(n, 'программист'+('ов' if n % 10 == 0 or 4 < n % 10 < 10 or 10 < n % 100 < 15 else 'а' if 1 < n % 10 < 5 else ''))

# more:

n = int(input())
k = n % 10
print(n, 'программист' + (('а', '')[k == 1], 'ов')[n % 100 // 10 == 1 or not(0 < k < 5)])
