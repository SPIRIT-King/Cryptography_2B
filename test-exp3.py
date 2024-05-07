def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(e, phi_n):
    g, x, _ = extended_gcd(e, phi_n)
    if g != 1:
        raise Exception('e 和 φ(n) 不互质，无法求模逆元')
    else:
        return x % phi_n

# 示例：假设e和φ(n)的值
e = 11  # 这是一个常用的公钥指数
phi_n = 192  # 假设的φ(n)值，实际应用中这会根据n具体计算得出

# 计算d
d = mod_inverse(e, phi_n)
print(f"d 的值是: {d}")