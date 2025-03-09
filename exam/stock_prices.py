def upward_trent(current_price, data, limit, result):
    if len(data) == 0:
        return

    if len(result) == 0:
        result.append(current_price)

    next_position = 0
    is_next_position = False

    for i in range(len(data)):
        if data[i] > current_price and data[i] - current_price <= limit:
            result.append(data[i])
            next_position = i
            is_next_position = True
            break

    if is_next_position:
        upward_trent(data[next_position], data[next_position + 1:], limit, result)

    else:
        return


stock_prices = []

for price in input().split(', '):
    stock_prices.append(int(price))

limit = int(input())
result_list = []
upward_trent(stock_prices[0], stock_prices[1:], limit, result_list)

print(*result_list)
