import random as rand


def main():
    height = 10
    width = 10
    number_of_generations = 100

    grid = create_grid(width, height)
    display_grid(grid, 0)
    for i in range(number_of_generations):
        grid = step_generation(grid, width, height)
        display_grid(grid, i + 1)


def create_grid(width: int, height: int) -> list:
    grid = []
    for i in range(height):
        grid.append([rand.randint(0, 1) for j in range(width)])
    return grid


def display_grid(grid: list, generation: int):
    for line in grid:
        line_buffer = ''
        for j in line:
            if j == 1:
                line_buffer += '█'
            else:
                line_buffer += '.'
            line_buffer += ' '
        print(line_buffer)
    print(f'Generation {generation}')


def step_generation(grid: list, width: int, height: int) -> list:
    for y_pos, line in enumerate(grid):
        for x_pos, cell in enumerate(line):
            living_adjacent_cell_count = number_of_live_adjacent_cells(grid, x_pos, y_pos, width, height)
            cell_state = grid[x_pos][y_pos]

            if living_adjacent_cell_count < 2 and cell_state == 1:
                grid[x_pos][y_pos] = 0
            elif living_adjacent_cell_count > 3 and cell_state == 1:
                grid[x_pos][y_pos] = 0
            elif living_adjacent_cell_count == 3 and cell_state == 0:
                grid[x_pos][y_pos] = 1

    return grid


def number_of_live_adjacent_cells(grid: list, x_pos: int, y_pos: int, grid_width: int, grid_height: int) -> int:
    adjacent_cell_positions = ((1, -1, 0, 0, 1, -1, -1, 1), (0, 0, 1, -1, 1, -1, 1, -1))
    live_cell_count = 0
    for i in range(8):
        x_pos_in_bounds = True
        y_pos_in_bounds = True
        if x_pos + adjacent_cell_positions[0][i] > grid_width - 1 or x_pos + adjacent_cell_positions[0][i] < 0:
            x_pos_in_bounds = False
        if y_pos + adjacent_cell_positions[1][i] > grid_height - 1 or y_pos + adjacent_cell_positions[1][i] < 0:
            y_pos_in_bounds = False

        if x_pos_in_bounds and y_pos_in_bounds:
            surrounding_cell = grid[x_pos + adjacent_cell_positions[0][i]][y_pos + adjacent_cell_positions[1][i]]
            if surrounding_cell == 1:
                live_cell_count += 1

    return live_cell_count


if __name__ == '__main__':
    main()

