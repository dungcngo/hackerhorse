def powMod(x,n,M):
	res = 1
	for _ in range(n):
		res = (res*x)%M
	return res

if __name__ == "__main__":
	x, n, M = 273246787654, 65536, 65537
	print(powMod(x, n, M))
