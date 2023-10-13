def get_combinations(curr, n, discount_rates, result):
    if len(curr) == n:
        result.append(curr[:])
        return

    for rate in discount_rates:
        curr.append(rate)
        get_combinations(curr, n, discount_rates, result)
        curr.pop()

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    combinations = []
    get_combinations([], len(emoticons), discount_rates, combinations)

    max_subscribers, max_sales = 0, 0

    for rates in combinations:
        total_subscribers, total_sales = 0, 0
        for user in users:
            total_price = 0
            for i, price in enumerate(emoticons):
                if rates[i] >= user[0]:
                    total_price += price * (1 - rates[i] / 100)

            if total_price >= user[1]:
                total_subscribers += 1
                total_price = 0

            total_sales += total_price

        if total_subscribers > max_subscribers:
            max_subscribers, max_sales = total_subscribers, total_sales
        elif total_subscribers == max_subscribers:
            max_sales = max(max_sales, total_sales)

    return [max_subscribers, int(max_sales)]
