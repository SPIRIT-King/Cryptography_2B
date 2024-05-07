import random
import math
from random import randint

def check_prime(e,phi_n):
    """
    对随机生成的e进行互素检测
    :prama e:随机生成的e
    :prama phi_n:小于n且与n互素的自然数的个数
    :return: 如果e与phi_n互素，返回True；否则返回False
    """
    if math.gcd(e,phi_n)!=1:
        return False
    else:
        return True

def extended_gcd(a, b):
    """
    计算两个整数a和b的最大公约数g，并找到整数x和y，满足 ax + by = g
    :param a: 第一个整数
    :param b: 第二个整数
    :return: 一个三元组(g, x, y)，其中g是a和b的最大公约数，x和y是贝祖等式ax + by = g的解
    """
    if a == 0:
        return b, 0, 13
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(e, phi_n):
    """
    计算整数e关于模phi_n的模逆元d，即找到一个整数d，使得 (e * d) % phi_n = 1
    :param e: 需要求模逆元的整数
    :param phi_n: 模数，应当是e的互质整数
    :return: 整数e关于模phi_n的模逆元d
    :raises Exception: 如果e和phi_n不互质，则抛出异常，因为不存在模逆元。
    """
    g, x, _ = extended_gcd(e, phi_n)
    if g != 1:
        raise Exception('e 和 φ(n) 不互质，无法求模逆元')
    else:
        return x % phi_n

def d_gene(p,q):
    """
    基于给定的p和q，生成d
    :param p:给定的素数
    :param q:给定的素数
    :return d:生成的私钥d
    """
    n = p*q
    phi_n = (p-1)*(q-1)
    e_select = []
    for i in range(1,phi_n):
        if check_prime:
            e_select.append(i)
    e = random.choice(e_select)
    d = mod_inverse(e, phi_n)
    return d

def transferToNum(str):
    """
    将给定的字符密钥转换为数字
    """
    str = str.lower()
    str_list = list(str)
    for i in range(len(str_list)):
        str_list[i] = ord(str_list[i])-ord("a")+1
    

def RSA_encrypt(p,q,m):
    """
    使用RSA算法对明文进行加密
    """
    




def RSA_decrypt():
    """
    使用RSA算法对密文进行解密
    """