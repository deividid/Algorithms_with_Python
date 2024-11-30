def get_paths(rows, columns, direction, lab, path):
    if rows >= len(lab) or columns >= len(lab[0]) or rows < 0 or columns < 0:
        return

    if lab[rows][columns] == "*":
        return

    if lab[rows][columns] == "v":
        return

    path.append(direction)

    if lab[rows][columns] == "e":
        print(''.join(path))

    else:
        lab[rows][columns] = "v"
        get_paths(rows + 1, columns, 'D', lab, path)
        get_paths(rows - 1, columns, 'U', lab, path)
        get_paths(rows, columns + 1, 'R', lab, path)
        get_paths(rows, columns - 1, 'L', lab, path)
        lab[rows][columns] = "-"

    path.pop()


rows = int(input())
columns = int(input())
labyrinth = [list(input()) for _ in range(rows)]


get_paths(0, 0, '', labyrinth, [])