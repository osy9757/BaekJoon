def mypow(b, e):
    ans = 1
    for i in range(e):
        ans = ans * b
    return ans

def main():
    ratio = float(input())

    if ratio > 10:
        print("No solution")
    else:
        answers = []

        ratio10000 = int(ratio * 10000 + 1e-8)

        for exp in range(8):
            for digit in range(1, 10):

                num = ratio10000 * digit * mypow(10, exp) - digit * mypow(10, 4)
                den = 100000 - ratio10000

                if den != 0 and num % den == 0:
                    oldval = digit * mypow(10, exp) + num // den
                    newval = 10 * num // den + digit
                    if abs(oldval * ratio - newval) < 1 and num // den < mypow(10, exp):
                        answers.append(digit * mypow(10, exp) + num // den)

        if len(answers) == 0:
            print("No solution")

        else:
            for answer in sorted(answers):
                print(answer)

if __name__ == "__main__":
    main()
