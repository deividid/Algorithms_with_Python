def get_corner(row, column, max_row, max_column, count):
    if row >= max_row or column >= max_column:
        return

    if row == max_row - 1 and column == max_column - 1:
        count.append(1)

    else:
        get_corner(row + 1, column, max_row, max_column, count)
        get_corner(row, column + 1, max_row, max_column, count)
        return len(count)


rows = int(input())
columns = int(input())

print(get_corner(0, 0, rows, columns, []))
