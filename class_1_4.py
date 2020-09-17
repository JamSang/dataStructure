def practice_4():
    last = 0
    for i in range(10, 1000):
        n = i
        a = 200 * n ** 3
        b = 2 ** n

        print(last)
        if last/(a-b) < 0:

            print(n)
            break
        last = a-b


def practice_5():
    n = 6*10**9
    t = 24* 60 *60

    a1 = n/t
    a2 = n*n /t
    print(a1,a2)

def main():
    practice_5()




if __name__ == '__main__':
    main()