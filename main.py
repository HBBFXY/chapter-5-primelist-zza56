def PrimeList(N):
    primes = []
    for num in range(2, N):
        is_prime = True
        # 检查num是否能被小于等于其平方根的数整除
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接所有质数字符串
    return ' '.join(primes)
