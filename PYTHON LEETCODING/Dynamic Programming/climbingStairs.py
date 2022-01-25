def climbStairs(n: int) -> int:
    dynamic_list = [int] * (n + 1)
    dynamic_list[n] = 1
    dynamic_list[n - 1] = 1

    for i in range(n - 2, -1, -1):
        dynamic_list[i] = dynamic_list[i + 1] + dynamic_list[i + 2]

    return dynamic_list[0]


if __name__ == "__main__":
    n = 5

    print(climbStairs(n))
