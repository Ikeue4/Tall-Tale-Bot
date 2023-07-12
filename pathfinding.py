import heapq

# Node class representing each cell in the grid
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g_cost = float('inf')  # cost from start node
        self.h_cost = 0  # heuristic cost to goal node
        self.f_cost = 0  # total cost: g_cost + h_cost
        self.is_wall = False
        self.parent = None

    def __lt__(self, other):
        return self.f_cost < other.f_cost


# A* pathfinding algorithm
def astar_pathfinding(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # Define the neighbors of a cell (up, down, left, right)
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Set the start node's cost and add it to the open set
    start_node = grid[start[0]][start[1]]
    start_node.g_cost = 0
    start_node.f_cost = start_node.h_cost
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node)

        # Check if the current node is the goal node
        if (current_node.row, current_node.col) == goal:
            # Reconstruct the path
            path = []
            while current_node.parent:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            path.append((start[0], start[1]))
            path.reverse()
            return path

        # Explore neighbors
        for dr, dc in neighbors:
            neighbor_row = current_node.row + dr
            neighbor_col = current_node.col + dc

            # Check if the neighbor is within the grid bounds
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                neighbor_node = grid[neighbor_row][neighbor_col]

                # Ignore walls and nodes in the closed set
                if neighbor_node.is_wall or neighbor_node in closed_set:
                    continue

                # Calculate the tentative cost from the start node to the neighbor node
                tentative_g_cost = current_node.g_cost + 1

                # Update the neighbor's cost if it's lower than the previous cost
                if tentative_g_cost < neighbor_node.g_cost:
                    neighbor_node.parent = current_node
                    neighbor_node.g_cost = tentative_g_cost
                    neighbor_node.h_cost = manhattan_distance(neighbor_row, neighbor_col, goal[0], goal[1])
                    neighbor_node.f_cost = neighbor_node.g_cost + neighbor_node.h_cost

                    # Add the neighbor to the open set if it's not already there
                    if neighbor_node not in open_set:
                        heapq.heappush(open_set, neighbor_node)

    # No path found
    return None


# Calculate Manhattan distance heuristic
def manhattan_distance(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)


# Grid setup example
def create_grid(rows, cols, walls):
    grid = []
    for row in range(rows):
        grid_row = []
        for col in range(cols):
            node = Node(row, col)
            if (row, col) in walls:
                node.is_wall = True
            grid_row.append(node)
        grid.append(grid_row)
    return grid


# Main function
def main():
    # Define the grid size and walls
    rows = 5
    cols = 5
    walls = [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

    # Create the grid
    grid = create_grid(rows, cols, walls)

    # Define the start and goal nodes
    start = (0, 0)
    goal = (4, 4)

    # Find the path using A* algorithm
    path = astar_pathfinding(grid, start, goal)

    # Print the path
    if path:
        print("Path found:")
        for row, col in path:
            print(f"({row}, {col})")
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
