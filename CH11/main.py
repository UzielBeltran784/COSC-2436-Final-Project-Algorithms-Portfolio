# ===========================================================================
# Knapsack Problem — Dynamic Programming
# ---------------------------------------------------------------------------
# Follow Instructions.md step by step. There are 11 TODOs total.
# Replace each "TODO N" block with the code shown in the instructions.
# Do NOT change the items list or the capacity at the bottom.
# ===========================================================================


# ---------------------------------------------------------------------------
# PART 1 — helper function
# ---------------------------------------------------------------------------
def calculate_total_value(solution, items):
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total


def knapsack(items, capacity):
    n = len(items)
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                grid[i][w] = grid[i - 1][w][:]
            else:
                include_solution = grid[i - 1][w - weight][:] + [item_name]
                exclude_solution = grid[i - 1][w][:]
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


def display_grid(grid, items):
    n = len(items)
    cell_width = 12

    header = ""
    for w in range(1, len(grid[0])):
        header += "{:>{width}}".format(str(w), width=cell_width)
    print(" " * cell_width + header)

    for i in range(1, n + 1):
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)

        for cell in grid[i][1:]:
            if cell:
                letters = "".join(name[0] for name in cell)
                value = calculate_total_value(cell, items)
                row += "{:>{width}}".format("${}({})".format(value, letters), width=cell_width)
            else:
                row += " " * cell_width

        print(row)


items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

grid = knapsack(items, capacity)
display_grid(grid, items)
