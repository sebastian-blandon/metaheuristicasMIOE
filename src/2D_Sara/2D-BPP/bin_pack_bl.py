from plot_bin_packing_bl import plot_bin_packing_bl


def bin_pack_bl(items, bin_capacity):
    """
    Packs items into a single bin using the Modified Bottom-Left (BL) algorithm with no item rotation.

    Args:
        items: A list of tuples representing items (width, height).
        bin_capacity: The capacity (area) of the bin.

    Returns:
        A tuple representing the single bin:
            (occupied_area, usable_empty_space, non_adjacent_area, bin_items, block_matrix).
    """

    bin_items = []  # Items placed in the bin
    current_occupied_area = 0
    block_matrix = [[0 for _ in range(bin_capacity[0])] for _ in range(bin_capacity[1])]

    sorted_items = items

    for item in sorted_items:
        item_width, item_height = item

        placed = False
        for y in range(bin_capacity[1]):
            for x in range(bin_capacity[0]):
                bottom_left = (x, y)
                if x + item_width <= bin_capacity[0] and y + item_height <= bin_capacity[1]:
                    if can_place(bin_items, bottom_left, item):
                        current_occupied_area += item_width * item_height
                        bin_items.append((bottom_left[0], bottom_left[1], item_width, item_height))
                        placed = True
                        
                        # Update block matrix
                        for i in range(item_height):
                            for j in range(item_width):
                                block_matrix[y + i][x + j] = 1
                        
                        break
            if placed:
                break
    
    usable_empty_space_Area =  count_zeros(block_matrix)


    return (usable_empty_space_Area,current_occupied_area, bin_items)


def calculate_usable_empty_space(bin_capacity, bin_items):
    """
    Calculates the usable empty space by considering projections of existing items to bin borders,
    taking into account potential overlaps between projections.

    Args:
        bin_capacity: The capacity (area) of the bin.
        bin_items: A list of tuples representing placed items (x, y, width, height).

    Returns:
        The usable empty space considering item projections, adjusted for potential overlaps.
    """

    usable_empty_space = 0
    seen_projections = set()  # Track seen projections to avoid double counting

    for item_x, item_y, item_width, item_height in bin_items:
        # Project to the left and right borders
        left_projection = min(item_x, bin_capacity[0] - (item_x + item_width))
        right_projection = min(item_x + item_width, bin_capacity[0] - item_x)

        # Consider only the first encountered projection on each side (avoid overlaps)
        if (item_x, 0) not in seen_projections:
            usable_empty_space += left_projection
            seen_projections.add((item_x, 0))
        if (item_x + item_width, 0) not in seen_projections:
            usable_empty_space += right_projection
            seen_projections.add((item_x + item_width, 0))

        # Project to the top and bottom borders
        top_projection = min(item_y, bin_capacity[1] - (item_y + item_height))
        bottom_projection = min(item_y + item_height, bin_capacity[1] - item_y)

        # Consider only the first encountered projection on each side (avoid overlaps)
        if (0, item_y) not in seen_projections:
            usable_empty_space += top_projection
            seen_projections.add((0, item_y))
        if (0, item_y + item_height) not in seen_projections:
            usable_empty_space += bottom_projection
            seen_projections.add((0, item_y + item_height))
        
        # Project to the top and bottom borders of the bin
        top_bin_projection = item_y
        bottom_bin_projection = bin_capacity[1] - (item_y + item_height)

        usable_empty_space += top_bin_projection + bottom_bin_projection

    return usable_empty_space

def can_place(bin_items, bottom_left, item):
    """
    Checks if an item can be placed at the given bottom-left corner 
    without overlapping existing items in the bin.

    Args:
        bin_items: A list of tuples representing bottom-left corner coordinates 
                   and dimensions of already placed items in the bin.
        bottom_left: A tuple representing the bottom-left corner coordinate 
                     where the item is to be placed.
        item: A tuple representing the item's dimensions (width, height).

    Returns:
        True if the item can be placed without overlap, False otherwise.
    """
    item_width, item_height = item
    item_right = bottom_left[0] + item_width
    item_top = bottom_left[1] + item_height

    for x, y, width, height in bin_items:
        if (x < item_right and x + width > bottom_left[0] and
                y < item_top and y + height > bottom_left[1]):
            return False
    return True

def count_zeros(matrix):
    count = 0
    for row in matrix:
        for i in range(len(row) - 1, -1, -1):  # Iterate from right to left
            if row[i] == 0:
                count += 1
            else:
                break  # Exit the loop when encountering a one
    return count

################################

## prueba de la funcion bin_pack_bl ##
if __name__ == "__main__":  # Definición para que no se ejecute desde el script principal
    
    dim = [[4, 6], [2, 8], [5, 3], [7, 2]]

    # order items randomly
    import random
    random.shuffle(dim)

    bin_capacity = [10, 20]

    packed_bin = bin_pack_bl(dim, bin_capacity)  # Use single_bin version



    print("Packed bin:")
    usable_empty_space_Area,occupied_area, item_placements = packed_bin
    print(f"Bin: Occupied Area = {occupied_area}, usable empty space Area = {usable_empty_space_Area}, Item Placements = {item_placements}")

    # Plot the first bin (index 0)
    plot_bin_packing_bl(bin_capacity, packed_bin)