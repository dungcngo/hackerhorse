def findGCD(a,b):
        if a == 0:
                return b
        return findGCD(b%a, a)

def main():
        a = 66528
        b = 52920
        g = findGCD(a, b)
        print(g)

if __name__ == "__main__":
        main()
